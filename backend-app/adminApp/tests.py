# adminApp/tests.py
from django.test import TestCase
from adminApp.services import DisputeService
from wallet.models import Wallet

class DisputeLogicTest(TestCase):
    def setUp(self):
        self.admin = User.objects.create_superuser(username="admin", password="123")
        self.client_user = User.objects.create_user(username="client", role="client")
        self.worker = User.objects.create_user(username="worker", role="worker")
        self.escrow = Escrow.objects.create(
            client=self.client_user, worker=self.worker, 
            total_amount=1000, worker_payout=900, status='disputed'
        )

    def test_dispute_resolved_in_favor_of_client(self):
        """When client wins, they get 1000 back, worker gets 0"""
        DisputeService.resolve(self.escrow.id, 'TOTAL_REFUND', self.admin)

        self.escrow.refresh_from_db()
        client_wallet = Wallet.objects.get(user=self.client_user)
        worker_wallet = Wallet.objects.get(user=self.worker)

        self.assertEqual(self.escrow.status, 'refunded')
        self.assertEqual(client_wallet.balance, 1000) # Full refund
        self.assertEqual(worker_wallet.balance, 0)    # Worker gets nothing