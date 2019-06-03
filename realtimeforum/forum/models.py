from django.db import models

# Create your models here.

class questions(models.Model):
    title =  models.CharField(max_length=191)
    slug =  models.CharField(max_length=191)
    body = models.TextField()
    category_id = models.IntegerField()
    user_id = models.IntegerField()
    created_at = models.DateField()
    updated_at = models.DateField()
    class Meta:
        db_table = 'questions'  # define your db name here

class categories(models.Model):
    name = models.TextField()
    slug = models.TextField()
    created_at = models.DateField()
    updated_at = models.DateField()

    class Meta:
        db_table = 'categories'







