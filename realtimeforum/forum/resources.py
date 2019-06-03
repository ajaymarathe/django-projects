from tastypie.resources import ModelResource
from forum.models import questions, categories

class QuestionResource(ModelResource):
    class Meta:
        queryset = questions.objects.all()
        resourece_name = 'question'

class CategoryResource(ModelResource):
    class Meta:
        queryset = categories.objects.all()
        resourece_name = 'category'