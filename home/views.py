from django.shortcuts import render
from menu.models import MenuCategory, MenuDish
from .models import PopularMenu


def home(request):
    categories = MenuCategory.objects.filter(is_visible=True)
    populas = PopularMenu.objects.filter(is_visible=True)
    context = {'categories': categories, 'populas': populas}
    for category in categories:
        category.dishes = MenuDish.objects.filter(category=category, is_visible=True)
    return render(request, 'home_index.html', context=context)


