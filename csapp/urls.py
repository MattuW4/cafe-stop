from . import views
from django.urls import path


urlpatterns = [
    path('', views.Index.as_view(), name='home'),
    path('browse', views.PostList.as_view(), name='browse'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('add', views.AddPost.as_view(), name='add'),
    path('post/update/<slug:slug>', views.UpdatePost.as_view(), name='update'),
    path('post/remove/<slug:slug>/', views.DeletePost.as_view(), name='delete'),
    # path('<slug:slug>/comment-update/<int:pk>', views.CommentEdit.as_view(),
    #      name='comment_edit'),
    ]
