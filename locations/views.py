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
