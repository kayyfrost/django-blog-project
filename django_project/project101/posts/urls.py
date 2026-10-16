from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.posts, name='list'),
    path('newPost/', views.newPost, name='newPost'),
    path('<slug:slug>', views.postPage, name='page')
]