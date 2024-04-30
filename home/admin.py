from django.contrib import admin
from .models import PopularMenu, BestPhrases
from django.utils.safestring import mark_safe


@admin.register(PopularMenu)
class PopularMenuAdmin(admin.ModelAdmin):
    '''
    This class is used to define the menu dish admin
    :param admin.ModelAdmin: This class is used to define the menu dish admin
    :type admin.ModelAdmin: class
    :return
    '''
    list_display = (
    'name', 'first_ingredient', 'second_ingredient', 'third_ingredient', 'price', 'image_src_tag', 'is_visible')
    list_editable = ('price',  'is_visible')
    list_filter = ('is_visible',)
    search_fields = ('name', 'first_ingredient', 'second_ingredient', 'third_ingredient')

    def image_src_tag(self, obj):
        """
        A function that generates an HTML img tag with the src attribute pointing to the URL of the photo.

        Parameters:
            obj (object): The object containing the photo information.

        Returns:
            str: An HTML img tag with the photo URL as the src attribute.
        """
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width=50 height=50>')

    image_src_tag.short_description = 'Popular dishes'


@admin.register(BestPhrases)
class BestPhrasesAdmin(admin.ModelAdmin):
    '''
    This class is used to define the best phrases admin
    :param admin.ModelAdmin: This class is used to define the best phrases admin
    :type admin.ModelAdmin: class
    :return
    '''
    list_display = ('phrase', 'author', 'position', 'photo_src_tag', 'is_visible')
    list_editable = ('author', 'is_visible', 'position')
    list_filter = ('is_visible',)
    search_fields = ('phrase', 'author')

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

    photo_src_tag.short_description = 'Best phrases'