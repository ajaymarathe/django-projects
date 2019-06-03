from django.db import models

# Create your models here.


class posts(models.Model):
    title = models.TextField()
    slug = models.TextField()
    body = models.TextField()
    category = models.TextField()
    user_id = models.IntegerField(null=True, blank=True)
    created_at = models.DateField(null=True, blank=True)
    updated_at = models.DateField(null=True, blank=True)
    class Meta:
        db_table = 'posts' #define your db here.


class comments(models.Model):
    body = models.TextField()
    user_id = models.IntegerField()
    # post_id = models.ForeignKey(posts, on_delete=models.CASCADE)

    post = models.ForeignKey(posts, on_delete=models.CASCADE)

    class Meta:
        db_table = 'comments' # define your db here.


