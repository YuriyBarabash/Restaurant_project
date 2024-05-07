from django.shortcuts import render
from .models import MenuCategory, SpecialProposals


def menu(request):
    """
        View function for the menu page.

        Retrieves menu categories from the database and renders the menu page
        with the obtained data.

        Parameters:
        - request (HttpRequest): The HTTP request object.

        Returns:
        - HttpResponse: The HTTP response containing the rendered menu page.

        Usage:
        This function is typically used as the view for the menu page URL.

        Example:
        # Define a URL pattern in urls.py:
        path('menu/', views.menu, name='menu')

        # Then create the corresponding template 'menu_index.html' in the templates directory.
        # The template can access the 'categories' variable.
        """

    categories = MenuCategory.objects.filter(is_visible=True)
    special_proposals = SpecialProposals.objects.filter(is_visible=True)
    context = {
        'categories': categories,
        'special_proposals': special_proposals
    }
    return render(request, 'menu_index.html', context=context)
