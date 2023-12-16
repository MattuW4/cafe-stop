from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.views.generic import CreateView
from django.contrib import messages
from csapp.models import Post, Comment, Category
from .forms import CommentForm, AddPostForm


class Index(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'


class PostList(generic.ListView):
    """
    View for displying all posts on browse page, filtering by approved
    and ordered by descending date to display 6 blog posts per page.
    """
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'browse.html'
    paginate_by = 6


class PostDetail(View):
    """
    View to post/get post detail to render on browse page,
    filtering posts by approved and ordered by most recent 
    date/time.
    """
    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('-created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm(),
            }
        )
    """
    View for post/get comment detail to render on browse page,
    filtering comments by approved and ordered by most recent
    date/time.
    """
    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('-created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm(),
            }
        )


class AddPost(CreateView):
    """
    View for adding a post.
    """
    model = Post
    form_class = AddPostForm
    template_name = 'post_add.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
        