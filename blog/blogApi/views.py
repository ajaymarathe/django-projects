from django.shortcuts import render

from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.core import serializers
import json


from .models import posts

# Create your views here.

def all_post(request):
    post = serializers.serialize("json", posts.objects.order_by('created_at'))
    data = {
            "results": {
                "data": post
                }
            }
    return JsonResponse(data)

def post_detail(request, pk):
    # post = serializers.serialize("json", posts.objects.get(pk=pk))
    post = posts.objects.all(pk=pk)
    # print(post)
    # return JsonResponse(post)
    data = {
        "results": {
            "data": post,
        }
    }
    return JsonResponse(data)