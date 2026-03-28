from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from django.test import TransactionTestCase
from django.db import transaction
from clients.models import Job
from escrow.models import Escrow
from wallet.models import Wallet
from unittest.mock import patch
from escrow.mpesa import MpesaC2B
from wallet.services import WalletService

User = get_user_model()

class EscrowFlowTests(APITestCase):
    def setUp(self):
        # Create users
        self.client_user = User.objects.create_user(username="c", role="client", phone_number="1")
        self.worker_user = User.objects.create_user(username="w", role="worker", phone_number="2")
        # Create a Job and Escrow record
        self.job = Job.objects.create(client=self.client_user, title="Fix Sink", budget=1000)
        self.escrow = Escrow.objects.create(
            job=self.job, client=self.client_user, worker=self.worker_user,
            total_amount=1000, platform_fee=100, worker_payout=900, status='held'
        )
        self.client.force_authenticate(user=self.client_user)

    def test_release_funds_updates_wallet(self):
        """Logic check: Client clicks release -> Wallet balance should change"""
        url = f"/api/escrow/transactions/{self.escrow.id}/release-funds/"
        response = self.client.post(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Check if worker wallet now has the money
        worker_wallet = Wallet.objects.get(user=self.worker_user)
        self.assertEqual(worker_wallet.balance, 900)
        
        # Check escrow status updated
        self.escrow.refresh_from_db()
        self.assertEqual(self.escrow.status, 'released')

class MpesaIntegrationTests(APITestCase):
    @patch('escrow.mpesa.requests.post') # Intercept the outgoing HTTP call
    def test_stk_push_trigger(self, mock_post):
        # Setup a fake success response from Safaricom
        mock_post.return_value.json.return_value = {"CheckoutRequestID": "ws_123", "ResponseCode": "0"}
        mock_post.return_value.status_code = 200

        client_api = MpesaC2B()
        response = client_api.stk_push("254712345678", 100, "REF123")
        
        self.assertEqual(response['CheckoutRequestID'], "ws_123")
        self.assertTrue(mock_post.called)

class AtomicEscrowTest(TransactionTestCase):
    def test_escrow_rollback_on_wallet_failure(self):
        """If WalletService fails, Escrow status should NOT change to 'released'"""
        escrow = Escrow.objects.create(status='held', total_amount=1000, worker_payout=900) # Fill required fields
        
        # We use a mock to deliberately raise an exception during wallet update
        with patch('wallet.services.WalletService.add_funds', side_effect=Exception("DB Connection Lost")):
            try:
                with transaction.atomic():
                    escrow.status = 'released'
                    escrow.save()
                    # This call will trigger the mocked Exception
                    WalletService.add_funds(escrow.worker, 900, 'payout', 'desc')
            except Exception:
                pass 

        # Refresh from DB to see if 'released' was rolled back
        escrow.refresh_from_db()
        self.assertEqual(escrow.status, 'held') # It stayed 'held' because of the rollback!

class EscrowPermissionTest(APITestCase):
    def setUp(self):
        self.worker = User.objects.create_user(username="worker_joe", role="worker")
        self.client_user = User.objects.create_user(username="client_jane", role="client")
        self.escrow = Escrow.objects.create(client=self.client_user, worker=self.worker, status='held', total_amount=1000, worker_payout=900)

    def test_worker_cannot_release_funds(self):
        """A worker attempting to release funds should get a 403 Forbidden"""
        self.client.force_authenticate(user=self.worker)
        url = f"/api/escrow/transactions/{self.escrow.id}/release-funds/"
        
        response = self.client.post(url)
        
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.escrow.refresh_from_db()
        self.assertNotEqual(self.escrow.status, 'released')
