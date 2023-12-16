from django import forms
from cloudinary.forms import CloudinaryFileField
from .models import Comment, Post


class AddPostForm(forms.ModelForm):
    """
    Uses forms to enable logged in and authenticated users to create posts and
    add to browse.html.
    """
    class Meta:
        model = Post
        fields = ['title', 'location', 'opening_time', 'closing_time',
                  'website', 'content', 'featured_image',]


class UpdatePostForm(forms.ModelForm):
    """
    Used forms and UpdatePost viw to enable a user to edit own blog post.
    """
    class Meta:
        model = Post
        fields = ['title', 'location', 'opening_time', 'closing_time',
                  'website', 'content', 'featured_image',]


class CommentForm(forms.ModelForm):
    """
    Uses forms to enable users to add comments to blog posts within the post
    detail view if they are logged in and authenticated.
    """
    class Meta:
        model = Comment
        fields = ('body',)
