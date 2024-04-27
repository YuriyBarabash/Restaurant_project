from django.contrib import admin
from .models import Chefs, HeadExpression, UnderChefsExpression
from django.utils.safestring import mark_safe


@admin.register(Chefs)
class ChefsAdmin(admin.ModelAdmin):
    '''
    This class is used to define the chefs admin
    :param admin.ModelAdmin: This class is used to define the chefs admin
    :type admin.ModelAdmin: class
    :return
    '''
    list_display = ('name', 'cuisine', 'position', 'photo_src_tag', 'is_visible')
    list_editable = ('position', 'is_visible')
    list_filter = ('is_visible',)
    search_fields = ('name', 'cuisine')

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

    photo_src_tag.short_description = 'Chef photo'


@admin.register(HeadExpression)
class HeadExpressionAdmin(admin.ModelAdmin):
    '''
    This class is used to define the head expression admin
    :param admin.ModelAdmin: This class is used to define the head expression admin
    :type admin.ModelAdmin: class
    :return
    '''
    list_display = ('name', 'job_title', 'expression', 'position', 'is_visible')
    list_editable = ('position', 'is_visible')
    list_filter = ('is_visible',)
    search_fields = ('name', 'job_title')


@admin.register(UnderChefsExpression)
class UnderChefsExpressionAdmin(admin.ModelAdmin):
    '''
    This class is used to define the under chefs expression admin
    :param admin.ModelAdmin: This class is used to define the under chefs expression admin
    :type admin.ModelAdmin: class
    :return
    '''
    list_display = ('name', 'job_title', 'expression', 'position', 'is_visible')
    list_editable = ('position', 'is_visible')
    list_filter = ('is_visible',)
    search_fields = ('name', 'job_title')















