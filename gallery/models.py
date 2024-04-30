from django.db import models


class GalleryCategory(models.Model):
    name = models.CharField(max_length=50, unique=True, db_index=True)
    is_visible = models.BooleanField(default=True)
    position = models.PositiveSmallIntegerField()

    class Meta:
        verbose_name_plural = 'Gallery Categories'
        ordering = ('position',)

    def __iter__(self):
        """
        A function that returns an iterator object for the given class instance.
        """
        for image in self.images.filter(is_visible=True):
            yield image

    def __str__(self):
        return self.name


class Gallery(models.Model):
    photo = models.ImageField(upload_to='gallery', blank=True)
    category = models.ForeignKey(GalleryCategory, on_delete=models.CASCADE, related_name='images', null=True)
    is_visible = models.BooleanField(default=True)
    position = models.PositiveSmallIntegerField()

    class Meta:
        verbose_name_plural = 'Gallery'
        ordering = ('position',)
        constraints = [
            models.UniqueConstraint(fields=['position', 'category'], name='unique_position_per_each_category_gallery'), ]


