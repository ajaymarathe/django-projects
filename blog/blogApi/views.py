from django.shortcuts import render

from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.core import serializers

from .models import posts, comments

# Create your views here.

# all post
def all_post(request):
    # post = posts.objects.all()
    post = serializers.serialize("json", posts.objects.order_by('created_at'))
    data = {
            "results": {
                "data": post
                }
            }
    return JsonResponse(data)

# specific post
def post_detail(request, pk):
    # print(pk)
    post = serializers.serialize("json", posts.objects.filter(pk=pk)) #specific post
    comment = serializers.serialize("json", comments.objects.filter(post=pk)) # all commment related to post
    # print(comment)
    data = {
        "results": {
            "data": post,
            "comment": comment
        }
    }
    return JsonResponse(data)



