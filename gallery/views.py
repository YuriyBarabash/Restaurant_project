from django.shortcuts import render


def gallery(request):
    return render(request, 'layout/gallery.html')
