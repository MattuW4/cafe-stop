from django.contrib import admin
from csapp.models import Post, Comment, Category
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """Admin post model"""
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content',
                     'location', 'opening_time', 'closing_time']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on')
    summernote_fields = ('content')
    actions = ['approve_posts']

    """Function to approve posts by admin"""
    def approve_posts(self, request, queryset):
        queryset.update(status='1')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """Admin comment model"""
    list_display = ('author', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ['author', 'body',
                     'location', 'opening_time', 'closing_time']
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)

"""Function for admin category model"""
admin.site.register(Category)
