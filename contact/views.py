from django.shortcuts import render
from .models import Address, FollowUs


def contact(request):
    address = Address.objects.all()
    follow_us = FollowUs.objects.all()
    context = {
        'address': address,
        'follow_us': follow_us,
    }
    return render(request, 'contact_index.html', context)
