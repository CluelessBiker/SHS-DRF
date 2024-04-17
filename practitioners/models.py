from django.db import models
from locations.models import Location
from services.models import Service
from languages.models import Language


class Practitioner(models.Model):
    """
    Practitioner details
    """
    locations = models.ManyToManyField(Location)
    services = models.ManyToManyField(Service)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    fName = models.CharField(max_length=50, blank=False, null=False)
    lName = models.CharField(max_length=50, blank=False, null=False)
    title = models.CharField(max_length=50, blank=False, null=False)
    bio = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='images/')
    personalExperience = models.TextField(blank=True, null=True)
    language = models.ForeignKey(
        Language,
        on_delete=models.SET_NULL,
        null=True,
    )
    primary = models.BooleanField(default=False, blank=False, null=False)

    class Meta:
        """ Ordering """
        ordering = ['primary']

    def __str__(self):
        """ Display text """
        return f"{self.fName} {self.lName} : {self.title}"
