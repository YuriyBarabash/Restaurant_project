from django.shortcuts import render, get_object_or_404
from .models import Blog


def blog(request):
    blog = Blog.objects.filter(is_published=True)
    context = {
        'blog': blog
    }
    return render(request, 'blog_index.html', context)


def blog_single_page(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    context = {
        'blog': blog,
        'blog_id': blog_id,
    }
    return render(request, 'blog_single_page_index.html', context)
