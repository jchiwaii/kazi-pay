from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()

class UserProfileTests(TestCase):
    def test_worker_profile_created_on_signup(self):
        """Tests that the signal correctly creates a WorkerProfile"""
        user = User.objects.create_user(
            username="worker1", 
            password="pass", 
            role="worker",
            phone_number="254712345678"
        )
        self.assertTrue(hasattr(user, 'workerprofile'))
        self.assertEqual(user.role, 'worker')

    def test_client_profile_created_on_signup(self):
        """Tests that the signal correctly creates a ClientProfile"""
        user = User.objects.create_user(
            username="client1", 
            password="pass", 
            role="client",
            phone_number="254700000000"
        )
        self.assertTrue(hasattr(user, 'clientprofile'))