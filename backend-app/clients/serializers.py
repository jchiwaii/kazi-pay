from rest_framework import serializers
from .models import Job
from workers.models import Bid # Assuming Bid model is in the worker app

class JobSerializer(serializers.ModelSerializer):
    client = serializers.ReadOnlyField(source='client.username')
    assigned_worker_name = serializers.ReadOnlyField(source='assigned_worker.username')
    bid_count = serializers.SerializerMethodField()

    class Meta:
        model = Job
        fields = [
            'id', 'client', 'title', 'description', 'price', 
            'status', 'assigned_worker', 'assigned_worker_name', 'bids', 'bid_count'            
        ]
        read_only_fields = ['client', 'status', 'assigned_worker']

    def get_bid_count(self, obj):
        return obj.bids.count()

class AcceptBidSerializer(serializers.Serializer):
    bid_id = serializers.IntegerField()