from . import views
from django.urls import path


urlpatterns = [
    path('', views.Index.as_view(), name='home'),
    path('browse', views.PostList.as_view(), name='browse'),
    ]
