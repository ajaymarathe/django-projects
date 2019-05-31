from django.db import models

# Create your models here.

class questions(models.Model):
    title =  models.CharField(max_length=191)
    body = models.TextField()
    class Meta:
        db_table = 'questions'  # define your custom name






