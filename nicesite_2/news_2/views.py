from django.shortcuts import render

from django.http import HttpResponse
from .models import *


def index(request):
    news = News.objects.all()
    categories = Category.objects.all()
    context = {
        'news': news,
        'title': 'Список новостей',
        'categories': categories,
    }
    return render(request, 'news_2/index.html', context)
    # return render(request, 'news_2/index.html')


def category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    categories = Category.objects.all()
    category = Category.objects.get(pk=category_id)
    context = {
        'news': news,
        'categories': categories,
        'category': category,
    }

    return render(request, 'news_2/category.html', context)
