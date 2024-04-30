from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class AboutSlider(models.Model):
    photo_hor = models.ImageField(upload_to='about/slider/')
    photo_vert = models.ImageField(upload_to='about/slider/')
    phrase = models.TextField()
    autor = models.CharField(max_length=50)
    is_visible = models.BooleanField(default=True)
    position = models.PositiveSmallIntegerField()

    class Meta:
        verbose_name_plural = 'About Slider'
        ordering = ('position',)

    def __str__(self):
        return self.phrase


class AboutRestaurant(models.Model):
    title = models.CharField(max_length=255)
    phrase = models.TextField()
    photo_chef = models.ImageField(upload_to='about/about_restaurant/')
    is_visible = models.BooleanField(default=True)
    position = models.PositiveSmallIntegerField()
    mark = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True, default=None, validators=[MinValueValidator(0), MaxValueValidator(5)])
    autor_mark = models.CharField(max_length=50, blank=True, null=True)
    authentic_phrase = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'About Restaurant'
        ordering = ('position',)

    def __str__(self):
        return self.phrase


class AboutSpecial(models.Model):
    title = models.CharField(max_length=255)
    phrase = models.TextField()
    photo = models.ImageField(upload_to='about/about_special/')
    is_visible = models.BooleanField(default=True)
    position = models.PositiveSmallIntegerField()

    class Meta:
        verbose_name_plural = 'About Special'
        ordering = ('position',)

    def __str__(self):
        return self.phrase


class AboutAwards(models.Model):
    logo = models.ImageField(upload_to='about/about_awards/')
    is_visible = models.BooleanField(default=True)
    position = models.PositiveSmallIntegerField()

    class Meta:
        verbose_name_plural = 'About Awards'
        ordering = ('position',)






