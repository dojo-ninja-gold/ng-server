from django.db import models
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models here.
class UserManager(models.Manager):
    def validate(self, data):
        errors = []
        if len(data['first_name']) < 2:
            errors.append('First name must be at least 2 characters long')
        if len(data['last_name']) < 2:
            errors.append('Last name must be at least 2 characters long')
        if not EMAIL_REGEX.match(data['email']):
            errors.append('Email must be valid')
        if len(data['password']) < 8:
            errors.append('Password must be at least 2 characters long')
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    pw_hash = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()