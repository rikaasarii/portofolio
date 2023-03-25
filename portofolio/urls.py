from django.urls import path
from . import views

urlpatterns =[
    path('', views.home, name="home"),
    path('posts/', views.posts, name="posts"),
    path('post/<str:pk>/', views.post, name="post"),
    path('profile/', views.profile, name="profile"),

    #crud path
    path('create_Post/', views.createPost,name="create_Post"),
    path('update_Post/<str:pk>/', views.updatePost,name="update_Post"),
    path('delete_Post/<str:pk>/', views.deletePost,name="delete_Post"),
]