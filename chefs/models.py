from django.db import models


class Chefs(models.Model):

    name = models.CharField(max_length=255, unique=True)
    cuisine = models.CharField(max_length=255, blank=True)
    position = models.PositiveSmallIntegerField()
    photo = models.ImageField(upload_to='chefs/', blank=True)
    is_visible = models.BooleanField(default=True)
    facebook = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    instagram = models.URLField(blank=True)

    class Meta:
        verbose_name_plural = 'Chefs'
        ordering = ('position',)

    def __str__(self) -> 'str':
        return self.name


class HeadExpression(models.Model):
    '''
    This class is used to define the head expression model
    :param models.Model: This class is used to define the head expression model
    :type models.Model: class
    :return
    '''
    expression = models.TextField()
    name = models.CharField(max_length=255, unique=True)
    job_title = models.CharField(max_length=255, blank=True)
    position = models.PositiveSmallIntegerField()
    is_visible = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Head Expressions'
        ordering = ('position',)

    def __str__(self) -> 'str':
        '''
        This method returns the name of the head expression
        :return: name of the head expression
        '''
        return self.name


class UnderChefsExpression(models.Model):
    expression = models.TextField()
    name = models.CharField(max_length=255, unique=True)
    job_title = models.CharField(max_length=255, blank=True)
    position = models.PositiveSmallIntegerField()
    is_visible = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Under Chefs Expressions'
        ordering = ('position',)

    def __str__(self) -> 'str':
        return self.name




