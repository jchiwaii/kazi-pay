from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Wallet
from .serializers import WalletSerializer
from .services import WalletService
from .mpesa import MpesaB2C

class WalletViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = WalletSerializer

    def get_queryset(self):
        return Wallet.objects.filter(user=self.request.user)

    @action(detail=False, methods=['post'], url_path='withdraw')
    def withdraw(self, request):
        amount = request.data.get('amount')
        try:
            
            MpesaB2C.pay_worker(
                phone=request.user.phone_number, 
                amount=amount, 
                remark="Withdrawal to M-Pesa"
            )
            
            WalletService.withdraw_funds(
                user=request.user, 
                amount=float(amount), 
                description="Withdrawal to M-Pesa"
            )
            return Response({"message": "Withdrawal processed successfully"})
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
    @action(detail=False, methods=['post'], url_path='balance')
    def check_balance(self, request):
        wallet = Wallet.objects.get(user=request.user)
        return Response({"balance": wallet.balance})