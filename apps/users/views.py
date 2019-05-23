from django.shortcuts import HttpResponse
from .models import User
from django.core import serializers
# Create your views here.
def show(req, user_id):
    user = User.objects.filter(id=user_id)
    json_user = serializers.serialize('json', user)
    return HttpResponse(json_user, status=200, content_type='application/json')

def create(req):
    pass

def login(req):
    pass