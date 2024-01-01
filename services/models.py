from django.db import models
from locations.models import Location


class Service(models.Model):
    """
    Services available
    """
    locations = models.ManyToManyField(Location)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=100, blank=False, null=False)
    blurb = models.CharField(max_length=250, blank=True, null=True)
    price = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
        blank=True,
    )
    duration = models.TimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='images/')

    class Meta:
        """ Ordering Services by title """
        ordering = ['title']

    def __str__(self):
        """ Display text """
        return f"{self.title}"
