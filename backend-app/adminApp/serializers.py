from rest_framework import serializers
from .models import PlatformRevenue, SystemAuditLog
from escrow.models import Escrow

class PlatformSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = PlatformRevenue
        fields = '__all__'

class DisputeResolutionSerializer(serializers.Serializer):
    escrow_id = serializers.IntegerField()
    winner_role = serializers.ChoiceField(choices=['worker', 'client'])