from .models import Comment, Post
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class PostForm(forms.ModelForm):
    """ This is a post form for the site"""
    class Meta:
        model = Post
        fields = (
            'title',
            'content',
            'featured_image',
        )