from rest_framework import serializers
from .models import Advertisement

class AdvertisementSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Advertisement
        fields = '__all__'
        read_only_fields = ('status', 'is_active', 'created_at', 'updated_at')

class AdvertisementCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisement
        fields = ('title', 'description', 'location', 'price', 'category')

    def create(self, validated_data):
        validated_data['owner'] = self.context['request'].user
        return super().create(validated_data)

class AdvertisementAdminSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Advertisement
        fields = '__all__'

    def update(self, instance, validated_data):
        # Only admin can update status
        if self.context['request'].user.role == 'admin':
            return super().update(instance, validated_data)
        else:
            # For regular users, only allow updating certain fields
            allowed_fields = {'title', 'description', 'location', 'price', 'category'}
            for field in list(validated_data.keys()):
                if field not in allowed_fields:
                    validated_data.pop(field)
            return super().update(instance, validated_data)