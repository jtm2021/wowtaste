pylint: disable=missing-module-docstring
pylint: disable=missing-function-docstring

from . import views
from django.urls import path


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('articles/', views.ArticlesList.as_view(), name='articles'),
    path('my_posts/', views.AddedPostsByUsers.as_view(), name='my_posts'),
    path('add_my_post/', views.AddMyPost.as_view(), name='add_my_post'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='blogpost_like'),
    path('<slug:slug>/update_my_post', views.UpdateMyPost.as_view(), name='update_my_post'),
    path('<slug:slug>/delete_my_post', views.DeleteMyPost.as_view(), name='delete_my_post'),
]
