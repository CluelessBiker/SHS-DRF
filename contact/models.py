from django.db import models


class Contact(models.Model):
    """
    Contact form
    """
    createdAt = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=False, null=False)
    subject = models.CharField(max_length=100, blank=False, null=False)
    message = models.TextField()
    email = models.CharField(max_length=100, blank=False, null=False)
    phone = models.CharField(max_length=100, blank=False, null=False)
    read = models.BooleanField(default=False, null=False, blank=False)

    class Meta:
        """ Ordering messages by date created """
        ordering = ['-createdAt']

    def __str__(self):
        """
        Formatted display text
        """
        return f"Sender: {self.name}; Subject: {self.subject}"
