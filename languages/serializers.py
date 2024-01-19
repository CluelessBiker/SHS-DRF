from rest_framework import serializers
from .models import Language


class LanguageSerializer(serializers.ModelSerializer):
    """ Language serilizer """
    class Meta:
        model = Language
        fields = [
            'id',
            'createdAt',
            'updatedAt',
            'code',
            'name',
        ]
