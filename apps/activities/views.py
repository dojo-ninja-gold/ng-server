from django.shortcuts import HttpResponse
from .models import Activity
from django.core import serializers

# Create your views here.
def index(req, user_id):
    activities = Activity.objects.filter(user=user_id)
    json_activities = serializers.serialize('json', activities)
    return HttpResponse(json_activities, status=200, content_type='application/json')

# def index_with_params(req):
#     print(req.GET)
#     return HttpResponse('params')