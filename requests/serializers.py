from rest_framework import serializers
from .models import RentRequest

class RentRequestSerializer(serializers.ModelSerializer):
    advertisement_title = serializers.ReadOnlyField(source='advertisement.title')
    requester_username = serializers.ReadOnlyField(source='requester.username')

    class Meta:
        model = RentRequest
        fields = '__all__'
        read_only_fields = ('requester', 'status', 'created_at', 'updated_at')

class RentRequestCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = RentRequest
        fields = ('advertisement', 'message')

    def validate_advertisement(self, value):
        if not value.is_active:
            raise serializers.ValidationError("This advertisement is no longer accepting requests.")
        if self.context['request'].user == value.owner:
            raise serializers.ValidationError("You cannot request your own advertisement.")
        return value

    def create(self, validated_data):
        validated_data['requester'] = self.context['request'].user
        return super().create(validated_data)

class RentRequestOwnerSerializer(serializers.ModelSerializer):
    requester_username = serializers.ReadOnlyField(source='requester.username')

    class Meta:
        model = RentRequest
        fields = '__all__'

    def update(self, instance, validated_data):
        # Only owner can update status
        if self.context['request'].user != instance.advertisement.owner:
            raise serializers.ValidationError("Only the advertisement owner can update request status.")
        return super().update(instance, validated_data)