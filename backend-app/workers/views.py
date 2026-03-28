from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .models import WorkerProfile, Bid
from .serializers import WorkerProfileSerializer, BidSerializer
from clients.models import Job
from clients.serializers import JobSerializer 
from rest_framework.decorators import action
from .services import WorkerService

class WorkerViewSet(viewsets.ModelViewSet):
    """Handles Worker Profile and Job Discovery"""
    serializer_class = WorkerProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return WorkerProfile.objects.filter(user=self.request.user)

class JobDiscoveryViewSet(viewsets.ReadOnlyModelViewSet):
    """Allows workers to see available jobs from all clients"""
    serializer_class = JobSerializer
    queryset = Job.objects.filter(status='open')

class BidViewSet(viewsets.ModelViewSet):
    """Allows workers to place and manage bids"""
    serializer_class = BidSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Bid.objects.filter(worker=self.request.user)

    def perform_create(self, serializer):
        # Use the service to create the bid
        WorkerService.place_bid(
            worker=self.request.user,
            job_id=self.request.data.get('job'),
            amount=self.request.data.get('amount'),
            proposal=self.request.data.get('proposal')
        )

    @action(detail=True, methods=['post'], url_path='mark-complete')
    def mark_complete(self, request, pk=None):
        bid = self.get_object() # This is the accepted bid
        try:
            WorkerService.complete_job(request.user, bid.job)
            return Response({"message": "Job marked as complete. Waiting for client approval."})
        except ValidationError as e:
            return Response({"error": str(e)}, status=400)