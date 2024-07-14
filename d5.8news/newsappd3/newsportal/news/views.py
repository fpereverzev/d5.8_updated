from django.shortcuts import render, redirect
from .forms import ArticleForm, PostForm
from .models import Article, Post

def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news:article_list')  # Замените на правильный путь
    else:
        form = ArticleForm()
    return render(request, 'news/create_article.html', {'form': form})

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news:post_list')  # Замените на правильный путь
    else:
        form = PostForm()
    return render(request, 'news/create_post.html', {'form': form})
