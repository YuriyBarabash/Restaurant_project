from django.contrib import admin
from .models import MenuCategory, MenuDish
from django.utils.safestring import mark_safe

@admin.register(MenuCategory)
class MenuCategoryAdmin(admin.ModelAdmin):
    '''
    This class is used to define the menu category admin
    :param admin.ModelAdmin: This class is used to define the menu category admin
    :type admin.ModelAdmin: class
    :return
    '''
    prepopulated_fields = {'slug': ('name',)}

@admin.register(MenuDish)
class MenuDishAdmin(admin.ModelAdmin):
    '''
    This class is used to define the menu dish admin
    :param admin.ModelAdmin: This class is used to define the menu dish admin
    :type admin.ModelAdmin: class
    :return
    '''
    list_display = (
    'name', 'category', 'position', 'slug', 'description', 'price', 'photo_src_tag', 'is_visible')
    list_editable = ('price', 'position', 'is_visible')
    list_filter = ('category', 'is_visible')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}

    def photo_src_tag(self, obj):
        """
        A function that generates an HTML img tag with the src attribute pointing to the URL of the photo.

        Parameters:
            obj (object): The object containing the photo information.

        Returns:
            str: An HTML img tag with the photo URL as the src attribute.
        """
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width=50 height=50>')

    photo_src_tag.short_description = 'Dish photo'
