from django.db import models
from django.conf import settings

class Escrow(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending Deposit'),
        ('held', 'Funds Held'),
        ('released', 'Funds Released'),
        ('refunded', 'Refunded to Client'),
        ('disputed', 'Under Dispute'),
    )

    job = models.OneToOneField('clients.Job', on_delete=models.CASCADE, related_name='escrow')
    client = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='payments_made')
    worker = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='payments_received')
    
    total_amount = models.DecimalField(max_digits=10, decimal_places=2) # What client paid
    platform_fee = models.DecimalField(max_digits=10, decimal_places=2) # Kazipesa's cut
    worker_payout = models.DecimalField(max_digits=10, decimal_places=2) # Net for worker
    
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    transaction_ref = models.CharField(max_length=100, blank=True, null=True) # e.g. M-Pesa ID

    dispute_reason = models.TextField(blank=True, null=True)
    disputed_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.SET_NULL, 
        null=True, 
        related_name='disputes_raised'
    )
    dispute_created_at = models.DateTimeField(null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Escrow for {self.job.title} - {self.status}"