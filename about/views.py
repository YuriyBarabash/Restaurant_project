from django.shortcuts import render
from django.views.generic import TemplateView
from .models import AboutSlider, AboutRestaurant, AboutSpecial, AboutAwards, AboutBottomSlider
from words_belt.models import WordsBelt


class About(TemplateView):
    """
        A view class to render the 'about_index.html' template with context data.

        Attributes:
            template_name (str): The name of the template to render.

        Methods:
            get_context_data(**kwargs): Retrieve the context data to be used when rendering the template.
        """

    template_name = 'about_index.html'

    def get_context_data(self, **kwargs):
        """
        Retrieve the context data to be used when rendering the template.

        Returns:
            dict: A dictionary containing the context data.
        """
        context = super().get_context_data(**kwargs)
        sliders_first = AboutSlider.objects.filter(is_visible=True)
        sliders_second = AboutRestaurant.objects.filter(is_visible=True)
        specials = AboutSpecial.objects.filter(is_visible=True)
        awards = AboutAwards.objects.filter(is_visible=True)
        words_belt = WordsBelt.objects.filter(is_visible=True)
        bottom_slider = AboutBottomSlider.objects.filter(is_visible=True)
        context['sliders_first'] = sliders_first
        context['sliders_second'] = sliders_second
        context['specials'] = specials
        context['awards'] = awards
        context['words_belt'] = words_belt
        context['bottom_slider'] = bottom_slider
        return context
