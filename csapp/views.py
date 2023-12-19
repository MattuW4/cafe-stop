from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse_lazy
from csapp.models import Post, Comment, Category
from .forms import CommentForm, AddPostForm, UpdatePostForm


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
    View to allow authenticated users to comment on posts.
    If statement checks if a user is logged in, input is
    valid and then authorises by admin to post."
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


# class CommentEdit(UserPassesTestMixin, generic.UpdateView):
#     """
#     View for updating/editing a comment.
#     """
#     model = Comment
#     template_name = 'comment_update.html'
#     fields = ['body']
#     form_class = UpdateCommentForm

#     def form_valid(self, form):
#         """Validate form after connecting form author to user"""
#         form.instance.author = self.request.user
#         return super().form_valid(form)

#     def test_func(self):
#         """Test that comment author is the same as logged in user"""
#         post = self.get_object()
#         if self.request.user == post.author:
#             return True
#         return False


class AddPost(CreateView):
    """
    View for adding a post.
    """
    model = Post
    form_class = AddPostForm
    template_name = 'post_add.html'

    def form_valid(self, form):
        """Validate form after connecting form author to user"""
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdatePost(UserPassesTestMixin, generic.UpdateView):
    """
    View for updating/editing a post.
    """
    model = Post
    template_name = 'post_update.html'
    form_class = UpdatePostForm

    def form_valid(self, form):
        """Validate form after connecting form author to user"""
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        """Test that comment author is the same as logged in user"""
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class DeletePost(UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('browse')

    def test_func(self):
        """Test that comment author is the same as logged in user"""
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class AddCategory(CreateView):
    """
    View for adding a category.
    """
    model = Category
    fields = '__all__'
    template_name = 'category_add.html'

    def form_valid(self, form):
        """Validate form after connecting form author to user"""
        form.instance.author = self.request.user
        return super().form_valid(form)


class SearchCategory(generic.ListView):
    """
    View for viewing categories.
    """
    model = Category
    template_name = 'categories.html'
    context_object_name = 'catalist'

    def get_queryset(self):
        content = {
            'cata': self.kwargs['category'],
            'posts': Post.objects.filter(category__name=self.kwargs
            ['category']).filter(status='1')
        }
        return content


    def form_valid(self, form):
        """Validate form after connecting form author to user"""
        form.instance.author = self.request.user
        return super().form_valid(form)

def category_list(request):
    category_list = Category.objects
    context = {
        'category_list': category_list,
    }
    return context