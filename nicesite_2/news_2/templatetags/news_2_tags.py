from django import template
from news_2.models import Category

register = template.Library()  # через этот обьект мы будем создовать пользовательские теги


@register.simple_tag(name='get_list_of_categories')
def get_categories():
    return Category.objects.all()


@register.inclusion_tag('news_2/list_categories.html')
def show_categories():
    categories = Category.objects.all()
    return {'categories': categories}


