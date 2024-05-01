from django.db import models


class Blog(models.Model):
    mark = models.CharField(max_length=100)
    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='blog', null=True, blank=True)
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Blog'
        ordering = ['-created_at']


