from django.shortcuts import render
from .models import StoryContent, StoryPhotos
from about.models import AboutAwards


def story(request):
    stories = StoryContent.objects.filter(is_visible=True)
    photos = StoryPhotos.objects.filter(is_visible=True)
    awards = AboutAwards.objects.filter(is_visible=True)
    context = {
        'stories': stories,
        'photos': photos,
        'awards': awards
    }
    return render(request, 'story_index.html', context=context)

