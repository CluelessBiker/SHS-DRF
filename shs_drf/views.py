from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view()
def root_route(request):
    """
    Display message when visiting API root url
    """
    return Response({
        "message": 'DRF API for System Health Spine'
    })
