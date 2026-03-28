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

# 2. Job Model (The Escrow Heart)
class Job(models.Model):
    STATUS_CHOICES = [
        ('PENDING_PAYMENT', 'Waiting for Client Deposit'),
        ('PAID', 'Funds in Escrow'),
        ('IN_PROGRESS', 'Worker Doing Job'),
        ('UNDER_REVIEW', 'Awaiting Client Approval'),
        ('COMPLETED', 'Funds Released to Worker'),
        ('CANCELLED', 'Cancelled/Refunded'),
        ('DISPUTED', 'Payment Held/Disputed'),
    ]
    
    # We use 'CustomUser' or 'settings.AUTH_USER_MODEL'
    client = models.ForeignKey('CustomUser', on_delete=models.CASCADE, related_name='jobs_posted')
    worker = models.ForeignKey('CustomUser', on_delete=models.SET_NULL, null=True, blank=True, related_name='jobs_taken')
    
    title = models.CharField(max_length=100)
    description = models.TextField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING_PAYMENT')
    
    # M-Pesa Tracking
    checkout_request_id = models.CharField(max_length=100, blank=True, null=True)
    mpesa_receipt = models.CharField(max_length=50, blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    accepted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.title} - {self.status}"

# 3. Job Application (The Matchmaking)
class JobApplication(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applications')
    worker = models.ForeignKey('CustomUser', on_delete=models.CASCADE, related_name='applications_made')
    note = models.TextField(blank=True)
    is_accepted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('job', 'worker')

# 4. Transaction Model (The Audit Trail)
class Transaction(models.Model):
    TYPE_CHOICES = [('DEPOSIT', 'Client Deposit'), ('PAYOUT', 'Worker Payout')]
    STATUS_CHOICES = [('SUCCESS', 'Success'), ('FAILED', 'Failed'), ('PENDING', 'Pending')]
    
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='transactions')
    transaction_type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    phone = models.CharField(max_length=15)
    
    # Detailed M-Pesa tracking for debugging
    checkout_request_id = models.CharField(max_length=100, blank=True, null=True)
    merchant_request_id = models.CharField(max_length=100, blank=True, null=True)
    mpesa_receipt = models.CharField(max_length=50, blank=True, null=True)
    result_description = models.TextField(blank=True, null=True)
    
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)