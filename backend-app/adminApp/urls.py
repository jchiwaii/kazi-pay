from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PlatformAdminViewSet

router = DefaultRouter()
router.register(r'control-panel', PlatformAdminViewSet, basename='admin-control')

urlpatterns = [
    path('', include(router.urls)),
]