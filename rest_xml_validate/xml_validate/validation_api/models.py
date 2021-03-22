from django.db import models

# Create your models here.


class MetaData(models.Model):
    data = models.TextField()
    version = models.FloatField()