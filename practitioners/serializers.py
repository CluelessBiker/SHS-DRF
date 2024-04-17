from rest_framework import serializers
from .models import Practitioner
from locations.serializers import LocationSerializer
from services.serializers import ServiceSerializer
from languages.serializers import LanguageSerializer


class PractitionerSerializer(serializers.ModelSerializer):
    """
    Serializer for Practitioner models
    """
    language = LanguageSerializer(many=True, read_only=True)
    locations = LocationSerializer(many=True, read_only=True)
    services = ServiceSerializer(many=True, read_only=True)

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
        model = Practitioner
        fields = [
            'id',
            'locations',
            'services',
            'createdAt',
            'updatedAt',
            'fName',
            'lName',
            'title',
            'bio',
            'image',
            'personalExperience',
            'language',
            'primary',
        ]


class PractitionerDetailSerializer(PractitionerSerializer):
    """
    Serializer for the Practitioner model used in Detail view
    Allow editing locations & services
    """
    language = serializers.ReadOnlyField(source='language.name')
    locations = LocationSerializer(many=True, read_only=True)
    services = ServiceSerializer(many=True, read_only=True)

    class Meta:
        model = Practitioner
        fields = [
            'id',
            'locations',
            'services',
            'createdAt',
            'updatedAt',
            'fName',
            'lName',
            'title',
            'bio',
            'image',
            'personalExperience',
        ]
