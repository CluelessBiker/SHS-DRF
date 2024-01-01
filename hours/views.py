from rest_framework import generics, permissions, status
from rest_framework.response import Response
from shs_drf.permissions import IsAdminOrReadOnly
from .models import Hour
from .serializers import HourSerializer, HourDetailSerializer


class HourList(generics.ListCreateAPIView):
    """
    List hours or create an entry if logged in & admin.
    """
    serializer_class = HourSerializer
    permission_classes = [
        IsAdminOrReadOnly,
        permissions.IsAuthenticatedOrReadOnly
    ]
    queryset = Hour.objects.all()

    def perform_create(self, serializer):
        """
        Creates a new entry,
        provided an entry for the same day does not
        already exist
        """
        location = serializer.validated_data['location']
        day = serializer.validated_data['day']

        existing_entry = Hour.objects.filter(location=location, day=day).first()
        if existing_entry:
            return Response(
                {'error': 'An entry with the same day already exists for this location.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer.save()

class HourDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve an entry/update/delete an entry
    if logged in & admin.
    """
    permission_classes = [
        IsAdminOrReadOnly,
        permissions.IsAuthenticatedOrReadOnly
    ]
    serializer_class = HourDetailSerializer
    queryset = Hour.objects.all()
