from django.shortcuts import render, redirect

from .forms import CommentForm, PostForm
from .models import Post, Comment

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'scribble/post_list.html', {'posts': posts})

def post_details(request):
    post.objects.get(pk=pk)
    return render(request, 'scribble/post_detail.html', )

def comment_list(request):
    comments = Comment.objects.all()
    return render(request, 'scribble/comment_list.html', {'comments': comments})

def post_delete(request, pk):
    post.object..get(pk=pk).delete()
    return.redirect