import random
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Blog


def blog(request):
    """
        View function to display a paginated list of published blogs.

        Args:
            request (HttpRequest): The HTTP request object.

        Returns:
            HttpResponse: The rendered response containing the paginated blog list.

        Raises:
            None
        """
    blog_list = Blog.objects.filter(is_published=True)
    paginator = Paginator(blog_list, 3)
    page = request.GET.get('page')
    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        blogs = paginator.page(1)
    except EmptyPage:
        blogs = paginator.page(paginator.num_pages)
    context = {
        'blogs': blogs
    }
    return render(request, 'blog_index.html', context)


def blog_single_page(request, blog_id):
    """
        View function to display a single blog post along with related posts.

        Args:
            request (HttpRequest): The HTTP request object.
            blog_id (int): The ID of the blog post to be displayed.

        Returns:
            HttpResponse: The rendered response containing the single blog post and related posts.

        Raises:
            Http404: If the requested blog post does not exist.
        """
    blog = get_object_or_404(Blog, id=blog_id)
    related_blogs = Blog.objects.filter(mark=blog.mark).exclude(id=blog_id)
    related_blogs_list = list(related_blogs)
    random_related_blogs = random.sample(related_blogs_list, min(len(related_blogs_list), 3))
    context = {
        'blog': blog,
        'blog_id': blog_id,
        'related_blogs': related_blogs,
        'random_related_blogs': random_related_blogs
    }
    return render(request, 'blog_single_page_index.html', context)
