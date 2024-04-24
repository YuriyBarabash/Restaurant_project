from django.db import models

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
    is_visible = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Dish Categories'
        ordering = ('position',)

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
    category = models.ForeignKey(MenuCategory, on_delete=models.CASCADE)
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

