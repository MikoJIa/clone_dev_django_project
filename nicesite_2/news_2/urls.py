from django.urls import path
from news_2 import views


urlpatterns = [
    path('', views.index, name='index'),
    path('test/', views.test, name='test')
]
