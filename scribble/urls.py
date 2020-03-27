from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='posts_list'),
    path()

    path('comments/new', views.comment_create, name='comment_create'),
]