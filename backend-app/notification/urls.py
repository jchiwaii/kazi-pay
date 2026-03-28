from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NotificationViewSet, ussd_callback, sms_callback

# 1. Initialize the router for the API
router = DefaultRouter()
router.register(r'', NotificationViewSet, basename='notification')

urlpatterns = [
    # 2. Add your Africa's Talking Webhooks FIRST
    # These must come before the router to ensure they are matched correctly
    path('ussd/', ussd_callback, name='ussd_callback'),
    path('incoming-sms/', sms_callback, name='sms_callback'),
    
    # 3. Include the router URLs for the rest of the notification API
    path('', include(router.urls)),
]