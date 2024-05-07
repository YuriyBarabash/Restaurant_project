from django.shortcuts import render
from .models import GalleryCategory


def gallery(request):
    """
        View function to render the gallery page with categories.

        Args:
            request (HttpRequest): The HTTP request object.

        Returns:
            HttpResponse: The HTTP response containing the rendered gallery page.
        """
    categories = GalleryCategory.objects.filter(is_visible=True)
    context = {
        'categories': categories
    }
    return render(request, 'index_gallery.html', context=context)

