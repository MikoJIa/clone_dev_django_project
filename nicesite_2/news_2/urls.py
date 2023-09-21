from django.urls import path
from news_2 import views


urlpatterns = [
    path('', views.index, name='index'),
    path('category/<int:category_id>/', views.category, name='category'),
    path('new/<slug:new_slug>/', views.view_new, name='view_new')
]
