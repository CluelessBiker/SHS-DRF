from rest_framework import generics, status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Language
from languages.serializers import LanguageSerializer
from shs_drf.permissions import IsAdminOrReadOnly


class LanguageList(generics.ListCreateAPIView):
    """
    List languages or create an entry if logged in & admin
    """
    serializer_class = LanguageSerializer
    permission_classes = [
        IsAdminOrReadOnly,
        permissions.IsAuthenticatedOrReadOnly,
    ]
    queryset = Language.objects.all()

    def perform_create(self, serializer):
        """
        Create a new Language
        """
        serializer.save()


class LanguageDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve/Update/Delete an entry if logged in & admin
    """
    permission_classes = [
        IsAdminOrReadOnly,
        permissions.IsAuthenticatedOrReadOnly
    ]
    serializer_class = LanguageSerializer
    queryset = Language.objects.all()
