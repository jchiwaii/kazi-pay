from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from wallet.models import Wallet

User = get_user_model()

class KazipesaBaseTestCase(APITestCase):
    """
    Base class for all Kazipesa tests. 
    Pre-configures a Client, a Worker, and an Admin.
    """
    def setUp(self):
        # 1. Create a Client
        self.client_user = User.objects.create_user(
            username="test_client", 
            role="client", 
            phone_number="254711111111",
            password="password123"
        )
        
        # 2. Create a Worker
        self.worker_user = User.objects.create_user(
            username="test_worker", 
            role="worker", 
            phone_number="254722222222",
            password="password123"
        )

        # 3. Create an Admin (Staff)
        self.admin_user = User.objects.create_superuser(
            username="test_admin", 
            role="admin", 
            phone_number="254733333333",
            password="password123"
        )

    def authenticate_as(self, user):
        """Helper to switch between users during a test"""
        self.client.force_authenticate(user=user)