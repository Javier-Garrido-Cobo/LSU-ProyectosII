from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class InfoRequest(models.Model):
    usuario = models.CharField(
        max_length=50,
        null=True
    )
    tema = models.CharField(
        max_length=50,
        null=False,
        blank=False,
    )
    descripcion = models.TextField(
        max_length=2000,
        null=False,
        blank=False
    )

