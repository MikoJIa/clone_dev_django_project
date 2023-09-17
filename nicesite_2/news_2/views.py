from django.shortcuts import render

from django.http import HttpResponse
from .models import News


def index(request):
    news = News.objects.all()
    context = {
        'news': news,
        'title': 'Список новостей'
    }
    return render(request, 'news_2/index.html', context)
    # return render(request, 'news_2/index.html')


def test(request):
    return HttpResponse(f"<h1>Тестовая страница</h1>")
