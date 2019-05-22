from django.shortcuts import HttpResponse
from .models import Activity
from django.core import serializers
import json

# Create your views here.
def index(req, user_id):
    activities = Activity.objects.filter(user=user_id).order_by('-created_at')
    json_activities = serializers.serialize('json', activities)
    return HttpResponse(json_activities, status=200, content_type='application/json')

# def index_with_params(req):
#     print(req.GET)
#     return HttpResponse('params')

def create(req):
    post_data = json.loads(req.body.decode())
    activity = Activity.objects.easy_create(post_data)
    # cannot serialize one single object
    # json_activity = serializers.serialize('json', activity)

    # OPTION 1 Turn singular activity into a list with one activity in it
    json_activities = serializers.serialize('json', [activity])
    print(json_activities)
    return HttpResponse(json_activities, status=200, content_type='application/json')