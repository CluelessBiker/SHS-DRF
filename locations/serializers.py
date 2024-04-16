from rest_framework import serializers
from .models import Location
from languages.serializers import LanguageSerializer


class LocationSerializer(serializers.ModelSerializer):
    language = LanguageSerializer(many=True, read_only=True)

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
        """
        Fields to display from model
        """
        model = Location
        fields = [
            'id',
            'createdAt',
            'updatedAt',
            'title',
            'phone',
            'email',
            'streetNum',
            'street',
            'city',
            'postcode',
            'gRating',
            'gMap',
            'image',
            'language',
            'area',
            'description',
        ]
