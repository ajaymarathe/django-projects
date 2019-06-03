from tastypie.resources import ModelResource
from blogApi.models import posts

from tastypie.authorization import Authorization


class PostsResource(ModelResource):
    class Meta:
        queryset = posts.objects.all()
        resource_name = 'posts'

        authorization = Authorization()