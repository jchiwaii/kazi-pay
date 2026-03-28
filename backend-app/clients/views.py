from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Job
from .serializers import JobSerializer, AcceptBidSerializer
from .services import JobService
from workers.models import Bid

class JobViewSet(viewsets.ModelViewSet):
    serializer_class = JobSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return Job.objects.none()
        # Clients only see jobs they posted, or 'open' jobs
        return Job.objects.filter(client=self.request.user)

    def perform_create(self, serializer):
        # Ensure the user posting is a client
        if self.request.user.role != 'client':
            return Response({"error": "Only clients can post jobs"}, status=403)
        serializer.save(client=self.request.user)

    @action(detail=True, methods=['post'], url_path='accept-bid')
    def accept_bid(self, request, pk=None):
        job = self.get_object()
        serializer = AcceptBidSerializer(data=request.data)
        
        if serializer.is_valid():
            bid_id = serializer.validated_data['bid_id']
            try:
                bid = Bid.objects.get(id=bid_id, job=job)
                JobService.accept_worker_bid(job, bid)
                return Response({"message": "Bid accepted and escrow initiated."}, status=status.HTTP_200_OK)
            except Bid.DoesNotExist:
                return Response({"error": "Bid not found for this job."}, status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)