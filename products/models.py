from django.db import models
from sqlalchemy import null

# Create your models here.


class Identified(models.Model):
    # name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='media', blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.timestamp
