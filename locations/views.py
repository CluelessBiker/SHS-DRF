from django.http import Http404
from rest_framework import generics, status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Location
from .serializers import LocationSerializer
from shs_drf.permissions import IsAdminOrReadOnly


class LocationList(generics.ListCreateAPIView):
    """
    List locations or create an entry if logged in & admin.
    """
    serializer_class = LocationSerializer
    permission_classes = [
        IsAdminOrReadOnly,
        permissions.IsAuthenticatedOrReadOnly,
    ]
    queryset = Location.objects.all()

    def perform_create(self, serializer):
        """
        Create a new location
        """
        if serializer.is_valid():
            if not self.request.user.is_staff:
                return Response(
                    {'detail': 'You do not have permission to perform this action'},
                    status=status.HTTP_403_FORBIDDEN
                )
            serializer.save()
            return Response(
                status=status.HTTP_201_CREATED
            )
        return Response(
            status=status.HTTP_400_BAD_REQUEST
        )


class LocationDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve an entry/update/delete an entry
    if logged in & admin.
    """
    permission_classes = [
        IsAdminOrReadOnly,
        permissions.IsAuthenticatedOrReadOnly
    ]
    serializer_class = LocationSerializer
    queryset = Location.objects.all()