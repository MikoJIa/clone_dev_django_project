from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse(f"<h1>Hello world!!!!!</h1>")


def test(request):
    return HttpResponse(f"<h1>Тестовая страница</h1>")
