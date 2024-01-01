from rest_framework import generics, permissions, status
from rest_framework.response import Response
from shs_drf.permissions import IsAdminOrReadOnly
from .models import Practitioner
from .serializers import PractitionerSerializer, PractitionerDetailSerializer


class PractitionerList(generics.ListCreateAPIView):
    """
    List Practitioners & create an entry if logged-in & admin
    """
    serializer_class = PractitionerSerializer
    permission_classes = [
        IsAdminOrReadOnly,
        permissions.IsAuthenticatedOrReadOnly
    ]
    queryset = Practitioner.objects.all()

    def perform_create(self, serializer):
        """
        Create a new Practitioner
        """
        serializer.save()


class PractitionerDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve/update/delete an entry
    if looged in & admin
    """
    permission_classes = [
        IsAdminOrReadOnly,
        permissions.IsAuthenticatedOrReadOnly
    ]
    serializer_class = PractitionerDetailSerializer
    queryset = Practitioner.objects.all()

