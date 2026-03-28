from django.db import models

class PlatformRevenue(models.Model):
    """Tracks total fees collected by Kazipesa"""
    total_fees_collected = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    total_payouts_processed = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Revenue: KES {self.total_fees_collected}"

class SystemAuditLog(models.Model):
    """Logs sensitive actions like manual escrow releases or dispute resolutions"""
    action_by = models.ForeignKey('authApp.CustomUser', on_delete=models.SET_NULL, null=True)
    action_type = models.CharField(max_length=100) # e.g., "MANUAL_ESCROW_RELEASE"
    details = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.action_type} at {self.timestamp}"