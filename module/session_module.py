import json

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from module.memory.memory_service import setCache, getCache


@csrf_exempt
def set_redis(request):
    dict_data = json.loads(request.body)
    key = dict_data["key"]
    value = dict_data["value"]
    setCache(key, value)
    return HttpResponse(content="success")


@csrf_exempt
def get_redis(request):
    dict_data = json.loads(request.body)
    key = dict_data["key"]
    vaule = getCache(key)
    return HttpResponse(content=vaule)
