from django.db import models
from ckeditor.fields import RichTextField


class Address(models.Model):
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Address'

    def __str__(self):
        return f"{self.street}, {self.city}, {self.country}"


class FollowUs(models.Model):
    mark = models.CharField(max_length=100)
    text = RichTextField()
    email = RichTextField()
    phone = RichTextField()
    social_media = RichTextField()

    class Meta:
        verbose_name_plural = 'Follow Us'


