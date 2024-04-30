from django.shortcuts import render
from .models import AboutSlider, AboutRestaurant, AboutSpecial, AboutAwards


def about(request):
    sliders_first = AboutSlider.objects.filter(is_visible=True)
    sliders_second = AboutRestaurant.objects.filter(is_visible=True)
    specials = AboutSpecial.objects.filter(is_visible=True)
    awards = AboutAwards.objects.filter(is_visible=True)
    context = {
        'sliders_first': sliders_first,
        'sliders_second': sliders_second,
        'specials': specials,
        'awards': awards
    }
    return render(request, 'about_index.html', context=context)