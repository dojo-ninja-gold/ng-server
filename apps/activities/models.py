from django.db import models
from ..locations.models import Location
from ..users.models import User
import random

# Create your models here.
class ActivityManager(models.Manager):
    def easy_create(self, post_data):
        user = User.objects.get(id=post_data['user_id'])
        location = Location.objects.get(id=post_data['location_id'])
        gold = random.randint(location.min_gold, location.max_gold)
        
        return Activity.objects.create(
            gold=gold,
            user=user,
            location=location
        )

class Activity(models.Model):
    gold = models.IntegerField()
    location = models.ForeignKey(Location, related_name='activities', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="activities", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ActivityManager()