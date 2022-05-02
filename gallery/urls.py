from django.urls import path
from django.views.decorators.cache import cache_page
from . import views

urlpatterns = [
    # path('', views.post_list, name='post_list'),
    path('', views.PostList.as_view(), name='post_list'),
    # path('<int:id>/', views.post_detail, name='post_detail'),
    path('create_post/', views.PostCreate.as_view(), name='create_post'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('<slug:slug>/update/', views.PostUpdate.as_view(), name='update_post'),
    path('<slug:slug>/delete/', views.PostDelete.as_view(), name='delete_post'),
    path('<slug:slug>/likes/', views.post_likes, name='post_likes'),
    # path('create_post/', views.create_post, name='create_post'),
    path('<slug:slug>/create_comment', views.create_comment, name='create_comment'),
]
