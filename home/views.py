from django.shortcuts import render
from menu.models import MenuCategory
from .models import PopularMenu


def home(request):
    """
        View function for the home page.

        Retrieves menu categories and popular menu items from the database
        and renders the home page with the obtained data.

        Parameters:
        - request (HttpRequest): The HTTP request object.

        Returns:
        - HttpResponse: The HTTP response containing the rendered home page.

        Usage:
        This function is typically used as the view for the home page URL.

        Example:
        # Define a URL pattern in urls.py:
        path('', views.home, name='home')

        # Then create the corresponding template 'home_index.html' in the templates directory.
        # The template can access the 'categories' and 'populas' variables.
        """
    categories = MenuCategory.objects.filter(is_visible=True)
    populas = PopularMenu.objects.filter(is_visible=True)
    context = {'categories': categories, 'populas': populas}
    return render(request, 'home_index.html', context=context)




