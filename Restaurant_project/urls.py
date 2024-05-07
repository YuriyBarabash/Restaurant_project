"""
URL configuration for Restaurant_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls')
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from home.views import home
from menu.views import menu
from about.views import About
from chefs.views import chefs
from gallery.views import gallery
from story.views import story
from contact.views import contact
from Restaurant_project import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('menu/', menu, name='menu'),
    path('about/', About.as_view(), name='about'),
    path('blog/', include('blog.urls')),
    path('chefs/', chefs, name='chefs'),
    path('gallery/', gallery, name='gallery'),
    path('story/', story, name='story'),
    path('contact/', contact, name='contact'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)