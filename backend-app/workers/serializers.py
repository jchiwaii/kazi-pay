from rest_framework import serializers
from .models import WorkerProfile, Bid
from clients.models import Job

class WorkerProfileSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='user.username')
    
    class Meta:
        model = WorkerProfile
        fields = ['username', 'skills', 'experience']

class BidSerializer(serializers.ModelSerializer):
    worker_name = serializers.ReadOnlyField(source='worker.username')
    
    class Meta:
        model = Bid
        fields = ['id', 'job', 'worker', 'worker_name', 'amount', 'proposal', 'is_accepted', 'created_at']
        read_only_fields = ['worker', 'is_accepted']