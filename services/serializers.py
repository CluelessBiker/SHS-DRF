from rest_framework import serializers
from .models import Service
from locations.serializers import LocationSerializer


class ServiceSerializer(serializers.ModelSerializer):
    """
    Serializer for Service models
    """
    class Meta:
        model = Service
        fields = [
            'id',
            'locations',
            'createdAt',
            'updatedAt',
            'title',
            'blurb',
            'description',
            'price',
            'image',
            'duration',
        ]


class ServiceDetailSerializer(ServiceSerializer):
    """
    Serializer for the Service model used in Detail view
    Allow editing locations
    """
    locations = LocationSerializer(many=True)  # Use LocationSerializer for editing locations

    class Meta:
        model = Service
        fields = [
            'id',
            'locations',
            'createdAt',
            'updatedAt',
            'title',
            'blurb',
            'description',
            'price',
            'image',
            'duration',
        ]
