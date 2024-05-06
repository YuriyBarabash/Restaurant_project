from django.db import models
from ckeditor.fields import RichTextField


class PopularMenu(models.Model):
    name = models.CharField(max_length=255)
    first_ingredient = models.CharField(max_length=50)
    second_ingredient = models.CharField(max_length=50)
    third_ingredient = models.CharField(max_length=50)
    image = models.ImageField(upload_to='popular_menu',blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    is_visible = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name_plural = 'Popular Dishes'
        ordering = ('-created_at',)

    def __str__(self):
        return self.name


class BestPhrases(models.Model):
    phrase = models.TextField()
    author = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='best_phrases', blank=True)
    position = models.PositiveSmallIntegerField(null=True, blank=True)
    is_visible = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Best Phrases'
        ordering = ('position',)

    def __str__(self):
        return self.phrase


class FooterItem(models.Model):
    address = RichTextField()
    phone = models.CharField(max_length=255)
    email = models.EmailField()
    working_hours = RichTextField()
    twitter = models.URLField(max_length=255, blank=True)
    facebook = models.URLField(max_length=255, blank=True)
    instagram = models.URLField(max_length=255, blank=True)
    youtube = models.URLField(max_length=255, blank=True)


