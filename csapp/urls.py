from . import views
from django.urls import path


urlpatterns = [
    path('', views.Index.as_view(), name='home'),
    path('browse', views.PostList.as_view(), name='browse'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('post_add', views.AddPostView.as_view(), name='post_add')
    ]
