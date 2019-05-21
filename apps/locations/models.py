from django.db import models

# Create your models here.
class LocationManager(models.Manager):
    pass

class Location(models.Model):
    name = models.CharField(max_length=255)
    min_gold = models.IntegerField()
    max_gold = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)