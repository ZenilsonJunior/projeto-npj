from unittest.util import _MAX_LENGTH

from django.db import models

# Create your models here.


class carla(models.Model):
    id = models.IntegerField(primary_key=True)
    senha = models.CharField(max_length=10)
