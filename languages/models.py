from django.db import models


class Language(models.Model):
    """ Site Language options """
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    code = models.CharField(
        null=False,
        unique=True,
        blank=False,
        max_length=2,
        verbose_name="Language Code",
    )
    name = model.CharField(
        null=False,
        unique=True,
        blank=False,
        max_length=25,
        verbose_name="Language name",
    )

    def Meta:
        verbose_name = "Language"
        verbose_name_plural = "Languages"
        oerdering = ['name']

    def __str__(self):
        """ Display Text """
        return f"{self.name} - {self.code}"
