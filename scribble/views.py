from django.shortcuts import render
from .models import Post, Comment

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'scribble/post_list.html', {'posts': posts})

def comment_list(request):
    comments = Comment.objects.all()
    return render(request, 'scribble/comment_list.html', {'comments': comments})