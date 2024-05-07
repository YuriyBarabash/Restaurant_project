from django.db import models


class WordsBelt(models.Model):
    """
        Model class representing words for the words belt.

        Attributes:
            word (TextField): The text of the word.
            position (IntegerField): The position of the word.
            is_visible (BooleanField): Indicates whether the word is visible or not.
        """
    word = models.TextField()
    position = models.IntegerField()
    is_visible = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Word`s Belt'
        ordering = ('position',)

    def __str__(self):
        return self.word

