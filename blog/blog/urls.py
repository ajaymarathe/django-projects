from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

# from blogApi.resources import PostsResource
# from blogApi.resources import CommentsResource

from blogApi.views import all_post, post_detail

# posts_resource = PostsResource()
# comments_resource = CommentsResource()

urlpatterns = [
    path('admin/', admin.site.urls),
    # url(r'^api/', include(posts_resource.urls)),
    # url(r'^api/', include(comments_resource.urls)),

    path("posts/", all_post, name="all_post"),
    path("posts/<int:pk>/", post_detail, name="post_detail")
]
