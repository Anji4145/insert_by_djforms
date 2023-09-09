from typing import Any
from django.db import models

# Create your models here.
class Marvel(models.Model):
    mname = models.CharField(max_length=10)
    mid = models.IntegerField(primary_key=True)
    mlan = models.CharField(max_length=10)

    def __str__(self):
        return self.mname