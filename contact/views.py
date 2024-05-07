from django.shortcuts import render
from .models import Address, FollowUs


def contact(request):
    """
       View function to render the contact page with address and follow us information.

       Args:
           request (HttpRequest): The HTTP request object.

       Returns:
           HttpResponse: The HTTP response containing the rendered contact page.
       """
    address = Address.objects.all()
    follow_us = FollowUs.objects.all()
    context = {
        'address': address,
        'follow_us': follow_us,
    }
    return render(request, 'contact_index.html', context)
