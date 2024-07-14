from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('articles/create/', views.create_article, name='create_article'),
    path('posts/create/', views.create_post, name='create_post'),
    # Добавьте другие URL-пути, если необходимо
]
