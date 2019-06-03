from django.db import models

# Create your models here.

class posts(models.Model):
    title = models.TextField()
    slug  = models.TextField()
    body = models.TextField()
    category = models.TextField()
    user_id = models.IntegerField()
    created_at = models.DateField(null=True, blank=True)
    updated_at = models.DateField(null=True, blank=True)

    class Meta:
        db_table = 'posts' #define your db here.

        # solution use ngif
