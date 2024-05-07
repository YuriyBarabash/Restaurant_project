from django.shortcuts import render
from .models import StoryContent, StoryPhotos
from about.models import AboutAwards


def story(request):
    """
        View function to render the story page with story content, photos, and awards.

        Args:
            request (HttpRequest): The HTTP request object.

        Returns:
            HttpResponse: The HTTP response containing the rendered story page.
        """
    stories = StoryContent.objects.filter(is_visible=True)
    photos = StoryPhotos.objects.filter(is_visible=True)
    awards = AboutAwards.objects.filter(is_visible=True)
    context = {
        'stories': stories,
        'photos': photos,
        'awards': awards
    }
    return render(request, 'story_index.html', context=context)

