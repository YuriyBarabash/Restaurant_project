from django.db import models


class WordsBelt(models.Model):
    word = models.TextField()
    position = models.IntegerField()
    is_visible = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Word`s Belt'
        ordering = ('position',)

    def __str__(self):
        return self.word

