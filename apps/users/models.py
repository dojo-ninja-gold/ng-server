from django.db import models
import re
import bcrypt
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

    def easy_create(self, data):
        # hash password
        hashed_pw = bcrypt.hashpw(data['password'].encode(), bcrypt.gensalt())
        print(hashed_pw)
        # create and return user
        return User.objects.create(
            first_name=data['first_name'],
            last_name=data['last_name'],
            email=data['email'],
            pw_hash=hashed_pw.decode()
        )

    def login(self, data):
        matching_users = User.objects.filter(email=data['email'])
        if matching_users:
            user = matching_users[0]
            if bcrypt.checkpw(data['password'].encode(), user.pw_hash.encode()):
                return (True, user)
        return (False, ["Email or password incorrect"])

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    gold = models.IntegerField(default=0)
    pw_hash = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()