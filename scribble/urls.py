# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.post_list, name='post_list'),
#     path('posts/<int:pk>', views.post_detail, name='post_detail'),
#     path('posts/new', views.post_create, name='post_create'),
#     path('posts/<int:pk>/edit', views.post_edit, name='post_edit'),
#     path('posts/<int:pk>/delete', views.post_delete, name='post_delete'),
#     path('comments/new', views.comment_create, name='comment_create'),
#     path('comments/<int:pk>/edit', views.comment_edit, name='comment_edit'),
#     path('comments/<int:pk>/delete', views.comment_delete, name='comment_delete'),
# ]


from django.urls import path
from . import views
# from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('posts/', views.PostList.as_view(), name='post_list'),
    path('posts/<int:pk>', views.PostDetail.as_view(), name='post_detail'),
    path('comments/', views.CommentList.as_view(), name='comment_list'),
    path('comments/<int:pk>', views.CommentDetail.as_view(), name='comment_detail'),
]