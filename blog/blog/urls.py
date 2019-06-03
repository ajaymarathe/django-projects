"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

from blogApi.resources import PostsResource

posts_resource = PostsResource()

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/', include(posts_resource.urls)),
    # to get all post use api/posts/ with get method
    # to make store post use api/posts/ with post method
    # to get specific post use api/posts/:id with get method
    # to update the post use api/posts/:id with put method
    # to delete the post use api/posts/:id with delete method
]
