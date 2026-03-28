from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from .models import PlatformRevenue
from .serializers import PlatformSummarySerializer, DisputeResolutionSerializer
from .services import AdminFinanceService, DisputeService
from rest_framework.views import APIView


class PlatformAdminViewSet(viewsets.ViewSet):
    permission_classes = [IsAdminUser]

    @action(detail=False, methods=['get'])
    def summary(self, request):
        revenue = PlatformRevenue.objects.first()
        serializer = PlatformSummarySerializer(revenue)
        return Response(serializer.data)

    @action(detail=False, methods=['post'], url_path='resolve-dispute')
    def resolve_dispute(self, request):
        serializer = DisputeResolutionSerializer(data=request.data)
        if serializer.is_valid():
            AdminFinanceService.resolve_dispute(
                escrow_id=serializer.validated_data['escrow_id'],
                winner_role=serializer.validated_data['winner_role'],
                admin_user=request.user
            )
            return Response({"message": "Dispute resolved and funds moved."})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class AdminResolveDisputeView(APIView):
    permission_classes = [IsAdminUser]

    def post(self, request, escrow_id):
        decision = request.data.get('decision') # 'TOTAL_REFUND' or 'TOTAL_PAYOUT'
        
        if decision not in ['TOTAL_REFUND', 'TOTAL_PAYOUT']:
            return Response({"error": "Invalid decision type"}, status=400)

        try:
            DisputeService.resolve(escrow_id, decision, request.user)
            return Response({"message": f"Dispute resolved successfully as {decision}"})
        except Exception as e:
            return Response({"error": str(e)}, status=400)