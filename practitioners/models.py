from django.db import models
from locations.models import Location
from services.models import Service


class Practitioner(models.Model):
    """
    Practitioner details
    """
    locations = models.ManyToManyField(Location)
    services = models.ManyToManyField(Services)
    createdAt = models.DateTimeField(auto_now_Add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    fName = modelsCharField(max_length=50, blank=False, null=False)
    lName = modelsCharField(max_length=50, blank=False, null=False)
    title = modelsCharField(max_length=50, blank=False, null=False)
    bio = models.TextField(blank-True, null=True)
    image = models.ImageField(upload_to='imgaes/')
    personalExperience = models.TextField()

    class Meta:
        """ Ordering """
        ordering = ['-createdAt']

    def __str__(self):
        """ Display text """
        return f"{self.fName} {self.lName} : {self.title}"
