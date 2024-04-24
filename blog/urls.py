from django.urls import path
from .views import blog, blog_single_page

app_name = 'blog'

urlpatterns = [
    path('', blog, name='blog'),
    path('blog_single_page/', blog_single_page, name='blog_single_page'),
    ]
