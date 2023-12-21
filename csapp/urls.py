from . import views
from django.urls import path


urlpatterns = [
    path('', views.Index.as_view(), name='home'),
    path('browse', views.PostList.as_view(), name='browse'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('add', views.AddPost.as_view(), name='add'),
    path('post/update/<slug:slug>', views.UpdatePost.as_view(), name='update'),
    # path('<slug:slug>/comment-edit/<int:pk>', views.CommentEdit.as_view(), name='comment_edit'),
    # path('<slug:slug>/comment-delete/<int:pk>', views.CommentDelete.as_view(), name='comment-delete'),
    path('post/<int:pk>/remove', views.DeletePost.as_view(), name='delete'),
    # path('add_category', views.AddCategory.as_view(), name='add_category'),
    path('category/<category>/', views.SearchCategory.as_view(), name='category_search'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='like_post')
    ]
