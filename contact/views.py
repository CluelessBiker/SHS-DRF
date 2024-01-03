from django.http import Http404
from rest_framework import generics, status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Contact
from .serializers import ContactSerializer
from shs_drf.permissions import IsAdminOrReadOnly


class ContactList(generics.ListCreateAPIView):
    """
    Restrict viewing of messages to Admin only
    Creation of contact message can be done by any one.
    """
    serializer_class = ContactSerializer

    def get_queryset(self):
        if self.request.user.is_staff:
            return Contact.objects.all()

    def perform_create(self, serializer):
        """
        submit a message
        """
        serializer.save()


class ContactDetail(generics.RetrieveDestroyAPIView):
    """
    Admin can retrieve all messages
    Admin can delete all messages
    Update not available.
    """
    permission_classes = [
        IsAdminOrReadOnly,
        permissions.IsAuthenticatedOrReadOnly
    ]
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
