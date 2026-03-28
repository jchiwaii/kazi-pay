from django.contrib import admin
from .models import Wallet, WalletTransaction

admin.site.register(Wallet)

@admin.register(WalletTransaction)
class WalletTransactionAdmin(admin.ModelAdmin):
    list_display = ('wallet', 'transaction_type', 'amount', 'timestamp')
    list_filter = ('transaction_type',)