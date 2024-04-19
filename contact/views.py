from django.http import Http404
from rest_framework import generics, status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Contact
from .serializers import ContactSerializer
from shs_drf.permissions import IsAdminOrReadOnly
from django.core.mail import BadHeaderError, send_mail
from django.conf import settings


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
        Send email to client via Django emails
        """
        instance = serializer.save()
        subject = f"SHS Contact Form : {instance.subject}"
        message = (
            "Senders details:\n"
            f"Name: {instance.name}\n"
            f"Email: {instance.email}\n"
            f"Phone: {instance.phone}\n\n"
            f"Subject: {instance.subject}\n"
            f"Message: {instance.message}"
        )
#         from_email = instance.email
        sender = f"Formal Name <{instance.email}>"
        to_email = [settings.DEFAULT_FROM_EMAIL]
        try:
            send_mail(
                subject,
                message,
#                 from_email,
                sender
                to_email,
            )
        except BadHeaderError as e:
            print(f"Error sending email: {e}")


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
