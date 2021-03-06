from rest_framework import serializers
from .models import Post, Comment

class PostSerializer(serializers.HyperlinkedModelSerializer):
    comments = serializers.HyperlinkedRelatedField(
        view_name='comment_detail',
        many=True,
        read_only=True
    )
    class Meta:
        model = Post
        fields = ('id', 'author', 'title', 'body', 'comments')

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    post = serializers.HyperlinkedRelatedField(
        view_name='post_detail',
        many=False,
        read_only=False,
        queryset=Post.objects.all(),
    )
    class Meta:
        model = Comment
        fields = ('id', 'author', 'body', 'post')