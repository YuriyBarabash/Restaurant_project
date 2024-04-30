from django.contrib import admin
from .models import Gallery, GalleryCategory
from django.utils.safestring import mark_safe


@admin.register(GalleryCategory)
class GalleryCategoryAdmin(admin.ModelAdmin):
    '''
    This class is used to define the gallery category admin
    :param admin.ModelAdmin: This class is used to define the gallery category admin
    :type admin.ModelAdmin: class
    :return
    '''
    list_display = ('name', 'position', 'is_visible')
    list_editable = ('position', 'is_visible')
    ordering = ('position',)


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    '''
    This class is used to define the gallery admin
    :param admin.ModelAdmin: This class is used to define the gallery admin
    :type admin.ModelAdmin: class
    :return
    '''
    list_display = ( 'photo_src_tag', 'category', 'position', 'is_visible')
    list_editable = ('position', 'is_visible')
    list_filter = ('is_visible', 'category')
    ordering = ('position',)

    def photo_src_tag(self, obj):
        """
        A function that generates an HTML img tag with the src attribute pointing to the URL of the photo.

        Parameters:
            obj (object): The object containing the photo information.

        Returns:
            str: An HTML img tag with the photo URL as the src attribute.
        """
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width=100 height=100>')

    photo_src_tag.short_description = 'Photo'
