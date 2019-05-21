from django.db import models
from ..locations.models import Location
from ..users.models import User

# Create your models here.
class ActivityManager(models.Manager):
    pass

class Activity(models.Model):
    gold = models.IntegerField()
    location = models.ForeignKey(Location, related_name='activities', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="activities", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)