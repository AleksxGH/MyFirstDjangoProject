from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm
from django.views.generic import DetailView, UpdateView, DeleteView
from datetime import datetime

def show_all(request):
    articles = Article.objects.all().order_by('-date') # Берем все статьи из базы данных

    # Получаем параметры фильтрации из GET-запроса
    author = request.GET.get('author')
    date = request.GET.get('date')
    resource = request.GET.get('resource')

    # Фильтрация (если пользователь ввел данные, фильтруем)
    if author:
        articles = articles.filter(author__icontains=author)
    if date:
        try:
            selected_date = datetime.strptime(date, "%Y-%m-%d").date()  # Оставляем только дату (без времени)
            articles = articles.filter(date__date=selected_date)  # Фильтрация без учета времени
        except ValueError:
            pass
    if resource:
        articles = articles.filter(resource__icontains=resource)

    # Получаем параметр сортировки
    sort_by = request.GET.get('sort')
    if sort_by:
        articles = articles.order_by(sort_by)

    return render(request, 'articles/all.html', {'articles': articles})

def create_article(request):
    error = ''
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all')
        else:
            error = 'Ошибка! Данные некорректны, попробуйте снова'

    form = ArticleForm
    data = {
        'form': form,
        'error': error
    }
    return render(request, "articles/new.html", data)

class ArticleDetailView(DetailView):
    model = Article
    template_name = "articles/article_layout.html"
    context_object_name = "article"

class ArticleUpdateView(UpdateView):
    model = Article
    template_name = "articles/new.html"
    form_class = ArticleForm

class ArticleDeleteView(DeleteView):
    model = Article
    template_name = "articles/delete.html"
    success_url = "/articles"