from django.shortcuts import render
from .models import Gallery, GalleryCategory


def gallery(request):
    categories = GalleryCategory.objects.filter(is_visible=True)
    context = {'categories': categories}
    return render(request, 'index_gallery.html', context=context)

