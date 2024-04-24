from django.shortcuts import render


def blog(request):
    return render(request, 'layout/blog.html')


def blog_single_page(request):
    return render(request, 'layout/blog_single_page.html')
