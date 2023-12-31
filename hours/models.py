from django.db import models
from locations.models import Location


class Hour(models.Model):
    """
    Set hours of operation for Location models
    """
    dayOfWeek = [
        ('mon', 'Monday'),
        ('tue', 'Tuesday'),
        ('wed', 'Wednesday'),
        ('thu', 'Thursday'),
        ('fri', 'Friday'),
        ('sat', 'Saturday'),
        ('sun', 'Sunday'),
    ]

    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    day = models.CharField(
        max_length=10,
        choices=dayOfWeek,
        default='mon',
        blank=False,
        null=False
    )
    open = models.TimeField()
    close = models.TimeField()
    info = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        """
        display text
        """
        return f"{self.day}: {self.open} - {self.close}"
