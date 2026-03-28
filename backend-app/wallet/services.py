# wallet/services.py
from django.db import transaction
from .models import Wallet, WalletTransaction

class WalletService:
    @staticmethod
    @transaction.atomic
    def add_funds(user, amount, tx_type, description, ref_id=None):
        wallet, created = Wallet.objects.get_or_create(user=user)
        wallet.balance += amount
        wallet.save()
        
        WalletTransaction.objects.create(
            wallet=wallet,
            transaction_type=tx_type,
            amount=amount,
            description=description,
            reference_id=ref_id
        )
        return wallet

    @staticmethod
    @transaction.atomic
    def withdraw_funds(user, amount, description, ref_id=None):
        wallet = user.wallet
        if wallet.balance < amount:
            raise ValueError("Insufficient balance")
        
        wallet.balance -= amount
        wallet.save()
        
        WalletTransaction.objects.create(
            wallet=wallet,
            transaction_type='withdrawal',
            amount=amount,
            description=description,
            reference_id=ref_id
        )
        return wallet