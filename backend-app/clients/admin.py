from django.contrib import admin
from .models import Job,ClientProfile

admin.site.register(ClientProfile)
@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'client',  'status','price')
    list_filter = ('status', 'client','price')
    search_fields = ('title', 'description', 'client__username')