from django.contrib import admin
from .models import WorkerProfile, Bid

admin.site.register(WorkerProfile)

@admin.register(Bid)
class BidAdmin(admin.ModelAdmin):
    list_display = ('job', 'worker', 'amount', 'is_accepted', 'created_at')
    list_filter = ('is_accepted',)