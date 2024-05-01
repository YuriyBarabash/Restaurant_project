from django.db import models


class StoryContent(models.Model):
    youtube_url = models.CharField(max_length=255)
    slogan = models.CharField(max_length=255)
    phrase = models.TextField()
    is_visible = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Content'


class StoryPhotos(models.Model):
    image = models.ImageField(upload_to='story_photos/')
    is_visible = models.BooleanField(default=True)
    position = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Photos'
        ordering = ('position',)







