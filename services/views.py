from rest_framework import generics, permissions, status
from rest_framework.response import Response
from shs_drf.permissions import IsAdminOrReadOnly
from .models import Service
from .serializers import ServiceSerializer, ServiceDetailSerializer


class ServiceList(generics.ListCreateAPIView):
    """
    List Services & create an entry if logged-in & admin
    """
    serializer_class = ServiceSerializer
    permission_classes = [
        IsAdminOrReadOnly,
        permissions.IsAuthenticatedOrReadOnly
    ]
    queryset = Service.objects.all()

    def perform_create(self, serializer):
        """
        Create a new Service
        """
        serializer.save()


class ServiceDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve/update/delete an entry
    if looged in & admin
    """
    permission_classes = [
        IsAdminOrReadOnly,
        permissions.IsAuthenticatedOrReadOnly
    ]
    serializer_class = ServiceDetailSerializer
    queryset = Service.objects.all()
