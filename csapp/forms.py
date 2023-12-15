from .models import Comment, Post
from django_summernote.widgets import SummernoteWidget
from django import forms 

class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'location',
            'opening_time',
            'closing_time',
            'website',
            'content',
            'featured_image',
        ]

        widgets = {
            'content': SummernoteWidget(),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
