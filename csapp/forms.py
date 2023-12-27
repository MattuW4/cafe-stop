from django import forms
from cloudinary.forms import CloudinaryFileField
from django_summernote.widgets import SummernoteWidget
from django.forms import ( MultiWidget, MultiValueField, TextInput, Textarea, URLInput)
from django.utils.translation import ugettext_lazy as _

from .models import Comment, Post


class AddPostForm(forms.ModelForm):
    """
    Uses forms to enable logged in and authenticated users to create posts and
    add to browse.html.
    """
    # website = forms.CharField(required=False)

    class Meta:
        model = Post
        fields = ['title', 'location', 'opening_time', 'closing_time',
                  'website', 'category', 'content', 'featured_image',]
        

        widgets = {
            'content': SummernoteWidget(),
            'title': forms.TextInput(attrs={
                'placeholder': 'Enter cafe name'
            }),
            'location': forms.TextInput(attrs={
                'placeholder': 'Enter the location e.g. Malham Cove, Yorkshire Dales'
            }),
            'website': forms.URLInput(attrs={
                'placeholder': 'Enter the links to their socials'
            }),
        }

        labels = {
            'title': _('Cafe name:'),
            'location': _('Cafe location:'),
            'opening_time': _('Cafe opening time:'),
            'closing_time': _('Cafe closing time:'),
            'website': _('Cafe website/socials (optional):'),
            'category': _('Category - select one from the drop down menu:'),
            'content': _('Description - tell us about your experience:'),
            'featured_image': _('Upload an image of the cafe:'),
        }

class UpdatePostForm(forms.ModelForm):
    """
    Used forms and UpdatePost view to enable a user to edit own blog post.
    """
    class Meta:
        model = Post
        fields = ['title', 'location', 'opening_time', 'closing_time',
                  'website', 'content', 'featured_image',]

        labels = {
            'title': _('Cafe name:'),
            'location': _('Cafe location:'),
            'opening_time': _('Cafe opening time:'),
            'closing_time': _('Cafe closing time:'),
            'website': _('Cafe website/socials (optional):'),
            'category': _('Category - select one from the drop down menu:'),
            'content': _('Description - tell us about your experience:'),
            'featured_image': _('Upload an image of the cafe:'),
        }


class CommentForm(forms.ModelForm):
    """
    Uses forms to enable users to add comments to blog posts within the post
    detail view if they are logged in and authenticated.
    """
    
    class Meta:
        model = Comment
        fields = ( 'body',)

        
    # def __init__(self, author, *args, **kwargs):
    #     super(CommentForm, self).__init__(*args, **kwargs)
    #     self.instance.author = author

        widgets = {
            'body': forms.Textarea(attrs={
                'placeholder': 'Get involved in the discussion - post a comment...'
            }),
        }

        labels = {
            
            'body': _(''),
        }

class EditCommentForm(forms.ModelForm):
    """
    Uses forms to enable users to add comments to blog posts within the post
    detail view if they are logged in and authenticated.
    """
    
    class Meta:
        model = Comment
        fields = ['author', 'body',]


