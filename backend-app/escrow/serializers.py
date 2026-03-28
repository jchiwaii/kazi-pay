
from rest_framework import serializers
from .models import Escrow

class EscrowSerializer(serializers.ModelSerializer):
    client_name = serializers.ReadOnlyField(source='client.username')
    worker_name = serializers.ReadOnlyField(source='worker.username')
    job_title = serializers.ReadOnlyField(source='job.title')

    class Meta:
        model = Escrow
        fields = [
            'id', 'job', 'job_title', 'client', 'client_name', 
            'worker', 'worker_name', 'total_amount', 
            'platform_fee', 'worker_payout', 'status', 'created_at'
        ]
        read_only_fields = ['platform_fee', 'worker_payout', 'status', 'client', 'worker']