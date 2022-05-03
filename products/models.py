from django.db import models
from sqlalchemy import null

# Create your models here.


class Identified(models.Models):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='media', blank=True, null=True)

    def __str__(self):
        return self.name
