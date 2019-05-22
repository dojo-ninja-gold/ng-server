from django.shortcuts import HttpResponse
from .models import Location
from django.core import serializers

# Create your views here.
def index(req):
    locations = Location.objects.all()
    json_locations = serializers.serialize('json', locations)
    return HttpResponse(json_locations, status=200, content_type="application/json")