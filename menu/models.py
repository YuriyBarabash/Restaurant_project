from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class MenuCategory(models.Model):
    '''
    This class is used to define the menu category model
    :param models.Model: This class is used to define the menu category model
    :type models.Model: class
    :return
    '''
    slug = models.SlugField(max_length=50, unique=True, db_index=True)
    name = models.CharField(max_length=50, unique=True)
    position = models.PositiveSmallIntegerField(unique=True)
    icon = models.CharField(max_length=50, blank=True)
    is_visible = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Dish Categories'
        ordering = ('position',)

    def __iter__(self):
        """
        A function that returns an iterator object for the given class instance.
        """
        for dish in self.dishes.filter(is_visible=True):
            yield dish


    def __str__(self) -> 'str':
        '''
        This method returns the name of the category
        :return: name of the category
        '''
        return self.name

class MenuDish(models.Model):
    '''
    This class is used to define the menu dish model
    :param models.Model: This class is used to define the menu dish model
    :type models.Model: class
    :return
    '''
    slug = models.SlugField(max_length=50, unique=True, db_index=True)
    name = models.CharField(max_length=255, unique=True)
    category = models.ForeignKey(MenuCategory, on_delete=models.CASCADE, related_name='dishes')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    position = models.PositiveSmallIntegerField()
    photo = models.ImageField(upload_to='menu_dishes/', blank=True)
    is_visible = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Dishes'
        ordering = ('position',)
        constraints = [
            models.UniqueConstraint(fields=['position', 'category'], name='unique_position_per_each_category'),]
        unique_together = ['id', 'slug']

    def __str__(self) -> 'str':
        '''
        This method returns the name of the dish
        :return: name of the dish
        '''
        return self.name


class SpecialProposals(models.Model):
    '''
    This class is used to define the special proposal model
    :param models.Model: This class is used to define the special proposal model
    :type models.Model: class
    :return
    '''
    slug = models.SlugField(max_length=50, unique=True, db_index=True)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    old_price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    photo = models.ImageField(upload_to='special_proposals/', blank=True)
    is_visible = models.BooleanField(default=True)
    mark = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True, default=None, validators=[MinValueValidator(0), MaxValueValidator(5)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Special Proposals'
        ordering = ('-created_at',)

    def __str__(self) -> 'str':
        '''
        This method returns the name of the special proposal
        :return: name of the special proposal
        '''
        return self.name

