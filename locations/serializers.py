from rest_framework import serializers
from .models import Location

class LocationSerializer(serializers.ModelSerializer):
    is_admin = serializers.SerializerMethodField()

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

    def get_is_admin(self, obj):
        """
        Check if user is an admin user
        """
        request = self.context['request']
        return request.user == request.user.is_staff

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
            'is_admin',
        ]
