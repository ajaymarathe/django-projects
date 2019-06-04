# from tastypie.resources import ModelResource
# from blogApi.models import posts, comments

# from tastypie.authorization import Authorization


# class PostsResource(ModelResource):
#     class Meta:
#         queryset = posts.objects.order_by('created_at')
#         # print(queryset)
#
#         resource_name = 'posts'
#         authorization = Authorization()
#
#
# class CommentsResource(ModelResource):
#
#     class Meta:
#         queryset = comments.objects.filter(post=6)
#         resource_name = 'comments'
#         authorization = Authorization()