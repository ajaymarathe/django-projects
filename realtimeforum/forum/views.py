from django.shortcuts import render
from forum.models import questions
# Create your views here.

def forum(request):
    questionsd = questions.objects.all()
    print(questionsd.__dict__)

    # questionsd = "hi how are you?"
    context = {
        "questionsd": questionsd,
    }
    return render(request, "index.html",context)
