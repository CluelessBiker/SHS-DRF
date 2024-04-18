from rest_framework import serializers
from .models import Contact


class ContactSerializer(serializers.ModelSerializer):
    """
    Serializer for the contact model
    """

    class Meta:
        model = Contact
        fields = [
            'id',
            'createdAt',
            'name',
            'phone',
            'email',
            'subject',
            'message',
            'read',
        ]
