from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    # Add your custom fields to the fieldsets so they show up in the admin
    fieldsets = UserAdmin.fieldsets + (
        ('Profile Info', {'fields': ('role', 'phone_number', 'national_id', 'is_verified')}),
    )
    list_display = ('phone_number', 'username', 'role', 'is_verified', 'is_staff')
    list_filter = ('role', 'is_verified')
    search_fields = ('phone_number', 'username', 'email')
    ordering = ('phone_number',)