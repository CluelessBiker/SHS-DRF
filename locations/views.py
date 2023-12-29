from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Location
from .serializers import LocationSerializer


class LocationList(APIView):
    """
    List all locations
    """
    def get(self, request):
        locations = Location.objects.all()
        serializer = LocationSerializer(locations, many=True)
        return Response(serializer.data)


class LocationDetail(APIView):
    """
    Return a single Location
    """
    serializer_class = LocationSerializer

    def get_object(self, pk):
        try:
            location = Location.objects.get(pk=pk)
            return location
        except Location.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        location = self.get_object(pk)
        serializer = LocationSerializer(location)
        return Response(serializer.data)

    def put(self, request, pk):
        location = self.get_object(pk)
        serializer = LocationSerializer(location, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)