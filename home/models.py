from django.db import models


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
    is_visible = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Best Phrases'
        ordering = ('-created_at',)

    def __str__(self):
        return self.phrase


