from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse
from .models import *


def index(request):
    news = News.objects.all()

    context = {
        'news': news,
        'title': 'Список новостей'
    }
    return render(request, 'news_2/index.html', context)
    # return render(request, 'news_2/index.html')


def category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)
    context = {
        'news': news,
        'category': category,
    }

    return render(request, 'news_2/category.html', context)


def view_new(request, new_slug):
    # new_item = News.objects.get(pk=new_slug)
    new_item = get_object_or_404(News, slug=new_slug)
    context = {
        'new_item': new_item,
    }
    return render(request, 'news_2/view_new.html', context)