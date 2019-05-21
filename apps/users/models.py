from django.db import models

# Create your models here.
class UserManager(models.Manager):
    pass

class User(models.Model):
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)