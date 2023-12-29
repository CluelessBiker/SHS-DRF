from rest_Framework import serializers
from .models import Location

class LocationSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

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
        ]
