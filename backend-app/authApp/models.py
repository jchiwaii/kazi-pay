from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Define the roles
    ROLE_CHOICES = (
        ('client', 'Client'),
        ('worker', 'Worker'),
        ('admin', 'Admin'),
    )
    
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='client')
    phone_number = models.CharField(max_length=15, unique=True, help_text="Enter M-Pesa linked number")
    national_id = models.CharField(max_length=20, blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    USERNAME_FIELD = 'phone_number' 
    REQUIRED_FIELDS = ['username', 'email']
    
    def __str__(self):
        return f"{self.username} ({self.role})"
