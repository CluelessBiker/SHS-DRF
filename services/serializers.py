from rest_framework import serializers
from .models import Service
from locations.serializers import LocationSerializer
from languages.serializers import LanguageSerializer


class ServiceSerializer(serializers.ModelSerializer):
    """
    Serializer for Service models
    """
    language = LanguageSerializer(read_only=True)
    locations = LocationSerializer(many=True, read_only=True)
    
    def validate_image(self, value):
            """
            Check image size
            """
            if value.size > 2 * 1024 * 1024:
                raise serializers.ValidationError('Image size larger than 2MB!')
            if value.image.height > 4096:
                raise serializers.ValidationError(
                    'Image height larger than 4096px!'
                )
            if value.image.width > 4096:
                raise serializers.ValidationError(
                    'Image width larger than 4096px!'
                )
            return value

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
            'language',
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
