from django.db import models
from languages.models import Language


class Location(models.Model):
    """ Business locations """
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=50, blank=False)
    phone = models.PositiveIntegerField(blank=False)
    email = models.EmailField()
    streetNum = models.CharField(max_length=50)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    postcode = models.PositiveIntegerField(blank=False)
    gRating = models.URLField()
    gMap = models.URLField()
    image = models.ImageField(upload_to='images/')
    language = models.ForeignKey(
        Language,
        on_delete=models.SET_NULL,
        null=True,
    )

    class Meta:
        """ Order locations by title """
        ordering = ['title']

    def __str__(self):
        """ Display text """
        return f"{self.title}'s location"
