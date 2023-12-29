from django.http import Http404
from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Location
from .serializers import LocationSerializer
from shs_drf.permissions import IsAdminOrReadOnly


class LocationList(APIView):
    """
    List all locations
    """
    serializer_class = LocationSerializer
    permission_classes = [
        IsAdminOrReadOnly,
        permissions.IsAuthenticatedOrReadOnly,
    ]

    def get(self, request):
        locations = Location.objects.all()
        serializer = LocationSerializer(
            locations,
            many=True,
            context={'request': request}
        )
        return Response(serializer.data)

    def post(self, request):
        """
        Create a new location
        """
        serializer = LocationSerializer(
            data=request.data, context={'request': request}
        )

        if serializer.is_valid():
            if not request.user.is_staff:
                return Response(
                    {'detail': 'You do not have permission to perform this action'},
                    status=status.HTTP_403_FORBIDDEN
                )
            serializer.save()
            return Response(
                serializer.data, status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.data, status=status.HTTP_400_BAD_REQUEST
        )


class LocationDetail(APIView):
    """
    Return a single Location
    """
    serializer_class = LocationSerializer
    permission_classes = [IsAdminOrReadOnly]

    def get_object(self, pk):
        try:
            location = Location.objects.get(pk=pk)
            self.check_object_permissions(self.request, location)
            return location
        except Location.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        location = self.get_object(pk)
        serializer = LocationSerializer(
            location,
            context={'request': request}
        )
        return Response(serializer.data)

    def put(self, request, pk):
        """
        Update an existing location
        """
        location = self.get_object(pk)
        serializer = LocationSerializer(
            location,
            data=request.data,
            context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """
        Delete an existing location
        """
        location = self.get_object(pk)
        post.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )