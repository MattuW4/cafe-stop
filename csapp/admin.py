from django.contrib import admin
from csapp.models import Post, Comment, Category
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """Admin post model"""
    summernote_fields = ('content')


class CommentAdmin(admin.ModelAdmin):
    """Admin comment model"""
    pass


class CategoryAdmin(admin.ModelAdmin):
    """Admin category model"""
    pass


admin.site.register(Comment, CommentAdmin)
admin.site.register(Category, CategoryAdmin)
