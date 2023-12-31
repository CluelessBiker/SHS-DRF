from rest_framework import serializers
from .models import Hour


class HourSerializer(serializers.ModelSerializer):
    """
    Serializer for the Hour model
    """

    class Meta:
        model = Hour
        fields = [
            'id',
            'location',
            'createdAt',
            'updatedAt',
            'day',
            'open',
            'close',
            'info'
        ]


class HourDetailSerializer(HourSerializer):
    """
    Serializer for the Hour model used in Detail view
    Location is a read only field so that we dont have to set it on each update
    """
    location = serializers.ReadOnlyField(source='location.id')