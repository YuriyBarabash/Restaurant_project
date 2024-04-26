from django.shortcuts import render
from .models import MenuCategory, MenuDish


def menu(request):
    categories = MenuCategory.objects.filter(is_visible=True)
    context = {'categories': categories}
    for category in categories:
        category.dishes = MenuDish.objects.filter(category=category, is_visible=True)
    return render(request, 'menu_index.html', context=context)