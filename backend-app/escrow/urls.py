from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EscrowViewSet, mpesa_callback

router = DefaultRouter()
router.register(r'transactions', EscrowViewSet, basename='escrow')

urlpatterns = [
    path('', include(router.urls)),
    path('mpesa-callback/', mpesa_callback, name='mpesa-callback'),
]