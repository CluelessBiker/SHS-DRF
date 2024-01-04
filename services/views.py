from rest_framework import generics, permissions, status, filters
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
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

    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]

    filterset_fields = [
        'location__title',
    ]

    search_fields = [
        'location__title',
        'location__city',
        'title',
    ]

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
