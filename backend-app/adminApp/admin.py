from django.contrib import admin
from .models import PlatformRevenue, SystemAuditLog

admin.site.register(PlatformRevenue)
admin.site.register(SystemAuditLog)