from django.shortcuts import render
from django.views import generic
from csapp.models import Post, Comment, Category


class PostList(generic.ListView):
    """
    View for displying all blog posts on blog page, filtering by approved 
    and ordered by descending date to display 6 blog posts per page.
    """
    model = Post
    queryset = Post.objects.all(status=1).order_by('-created_on')
    template_name = "index.html"
    paginate_by = 6
