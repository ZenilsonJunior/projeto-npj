from unittest.util import _MAX_LENGTH

from django.db import models

# Create your models here.


class User(models.Model):
    username = models.IntegerField(primary_key=True)
    email = models.EmailField
    senha = models.CharField(max_length=10)
