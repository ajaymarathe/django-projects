# Create your views here.

from django.shortcuts import render
from blog.models import Post
from blog.forms import CommentForm
from blog.models import Post, Comment, Questions

# index view
def blog_index(request):
    posts = Post.objects.all().order_by('-created_on')
    context = {
        "posts": posts,
    }
    return render(request, "blog_index.html", context)

# category view
def blog_category(request, category):
    posts = Post.objects.filter(categories__name__contains=category)\
        .order_by('-created_on')

    context = {
        "category": category,
        "posts": posts
    }
    return render(request, "blog_category.html", context)

# blog detail
def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)

    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post
            )
            comment.save()

    comments = Comment.objects.filter(post=post)
    context = {"post": post, "comments": comments, "form": form}

    return render(request, "blog_detail.html", context)

def forum(request):
    questions = Questions.objects.all()
    context = {
        "questions": questions,
    }
    return render(request, "index.html",context)


