from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WorkerViewSet, JobDiscoveryViewSet, BidViewSet

router = DefaultRouter()
router.register(r'profile', WorkerViewSet, basename='worker-profile')
router.register(r'browse-jobs', JobDiscoveryViewSet, basename='browse-jobs')
router.register(r'my-bids', BidViewSet, basename='worker-bids')

urlpatterns = [
    path('', include(router.urls)),
]