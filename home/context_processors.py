from .models import FooterItem


def footer_items(request):
    """
        Retrieve footer items to be displayed in the footer.

        Args:
            request (HttpRequest): The HTTP request object.

        Returns:
            dict: A dictionary containing the footer items.
        """
    return {
        'footer_items': FooterItem.objects.first()
    }