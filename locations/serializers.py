from rest_framework import serializers
from .models import Location

class LocationSerializer(serializers.ModelSerializer):
    is_admin = serializers.SerializerMethodField()

    def get_is_admin(self, obj):
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
