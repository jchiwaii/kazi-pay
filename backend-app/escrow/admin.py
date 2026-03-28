from django.contrib import admin
from .models import Escrow

@admin.register(Escrow)
class EscrowAdmin(admin.ModelAdmin):
    list_display = ('job', 'client', 'worker', 'total_amount', 'status', 'transaction_ref')
    list_filter = ('status', 'created_at')
    readonly_fields = ('transaction_ref',) # Prevent accidental tampering with M-Pesa refs