from datetime import timezone

from rest_framework import viewsets, status, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Escrow
from .serializers import EscrowSerializer
from wallet.services import WalletService
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from django.db import models
from notification.services import NotificationService

class EscrowViewSet(viewsets.ModelViewSet):

    serializer_class = EscrowSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Users should only see escrows they are involved in
        user = self.request.user
        return Escrow.objects.filter(models.Q(client=user) | models.Q(worker=user))

    @action(detail=True, methods=['post'], url_path='release-funds')
    def release_funds(self, request, pk=None):
        """
        Action for the CLIENT to release money to the worker.
        """
        escrow = self.get_object()

        # 1. Validation: Only the client who posted the job can release funds
        if escrow.client != request.user:
            return Response({"error": "Unauthorized. Only the client can release funds."}, 
                            status=status.HTTP_403_FORBIDDEN)

        # 2. Validation: Can't release if funds aren't held or already released
        if escrow.status != 'held':
            return Response({"error": f"Cannot release funds. Current status: {escrow.status}"}, 
                            status=status.HTTP_400_BAD_REQUEST)

        # 3. Atomic Update (The Handshake)
        escrow.status = 'released'
        escrow.save()
        
        # Update Job Status in the client app
        job = escrow.job
        job.status = 'completed'
        job.save()

        WalletService.add_funds(
            user=escrow.worker,
            amount=escrow.worker_payout,
            tx_type='escrow_payout',
            description=f"Payment for job: {escrow.job.title}",
            ref_id=f"ESC-{escrow.id}"
        )
        
        return Response({"message": "Funds released successfully to the worker."}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'], url_path='raise-dispute')
    def raise_dispute(self, request, pk=None):
        escrow = self.get_object()
        reason = request.data.get('reason')

        if escrow.status not in ['held', 'completed_by_worker']:
            return Response({"error": "Cannot dispute this transaction now."}, status=400)

        escrow.status = 'disputed'
        escrow.dispute_reason = reason
        escrow.disputed_by = request.user
        escrow.dispute_created_at = timezone.now()
        escrow.save()

        NotificationService.send(
            recipient=escrow.worker if request.user == escrow.client else escrow.client,
            title="Escrow Dispute Raised",
            message=f"A dispute has been raised for the job: {escrow.job.title}. Reason: {reason}"
        )

        return Response({"message": "Dispute raised. Admin will contact both parties."})
    


@api_view(['POST'])
@permission_classes([AllowAny])
def mpesa_callback(request):
    stk_callback = request.data.get('Body', {}).get('stkCallback', {})
    result_code = stk_callback.get('ResultCode')
    checkout_id = stk_callback.get('CheckoutRequestID')

    if result_code == 0:
        # Success logic: Update Escrow to 'held'
        # Extract Receipt Number from CallbackMetadata
        items = stk_callback.get('CallbackMetadata', {}).get('Item', [])
        receipt = next(item['Value'] for item in items if item['Name'] == 'MpesaReceiptNumber')
        
        escrow = Escrow.objects.get(checkout_request_id=checkout_id)
        escrow.status = 'held'
        escrow.transaction_ref = receipt
        escrow.save()
        
    return Response({"ResultCode": 0, "ResultDesc": "Success"})