from django.shortcuts import render


def chefs(request):
    return render(request, 'layout/chefs.html')
