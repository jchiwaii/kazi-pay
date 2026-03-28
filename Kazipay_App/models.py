from django.db import models
from django.contrib.auth.models import User

# 1. User Profile (Binary Role)
class Profile(models.Model):
    ROLE_CHOICES = [
        ('CLIENT', 'Client'),
        ('WORKER', 'Worker'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phone_number = models.CharField(max_length=15, unique=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=5.0)

    def __str__(self):
        return f"{self.user.username} - {self.role}"

# 2. Job Model (The Escrow Heart)
class Job(models.Model):
    STATUS_CHOICES = [
        ('PENDING_PAYMENT', 'Waiting for Client Deposit'),
        ('PAID', 'Funds in Escrow'), # Payment successful via STK Push
        ('IN_PROGRESS', 'Worker Doing Job'),
        ('UNDER_REVIEW', 'Awaiting Client Approval'), # Worker clicked "Done"
        ('COMPLETED', 'Funds Released to Worker'),
        ('CANCELLED', 'Cancelled/Refunded'),
        ('DISPUTED', 'Payment Held/Disputed'),
    ]
    
    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='jobs_created')
    worker = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='jobs_assigned')
    
    title = models.CharField(max_length=100)
    description = models.TextField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING_PAYMENT')
    
    # M-Pesa Tracking (Stored on Job for easy state check)
    checkout_request_id = models.CharField(max_length=100, blank=True, null=True)
    mpesa_receipt = models.CharField(max_length=50, blank=True, null=True)
    
    accepted_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Job {self.id}: {self.title}"

# 3. Job Application (The Matchmaking)
class JobApplication(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applications')
    worker = models.ForeignKey(User, on_delete=models.CASCADE, related_name='job_applications')
    note = models.TextField(blank=True, help_text="Worker's pitch to the client")
    is_accepted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('job', 'worker') # Worker applies only once

# 4. Transaction Model (The Financial Audit Trail)
class Transaction(models.Model):
    TYPE_CHOICES = [('DEPOSIT', 'Client Deposit'), ('PAYOUT', 'Worker Payout')]
    STATUS_CHOICES = [('SUCCESS', 'Success'), ('FAILED', 'Failed'), ('PENDING', 'Pending')]
    
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='transactions')
    transaction_type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    phone = models.CharField(max_length=15)
    
    # Detailed M-Pesa tracking
    checkout_request_id = models.CharField(max_length=100, blank=True, null=True)
    merchant_request_id = models.CharField(max_length=100, blank=True, null=True)
    mpesa_receipt = models.CharField(max_length=50, blank=True, null=True)
    result_description = models.TextField(blank=True, null=True) 
    
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)
