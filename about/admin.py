from django.contrib import admin
from .models import AboutSlider, AboutRestaurant, AboutSpecial, AboutAwards, AboutBottomSlider
from django.utils.safestring import mark_safe


@admin.register(AboutSlider)
class AboutSliderAdmin(admin.ModelAdmin):
    '''
    This class is used to define the admin panel for the AboutSlider model
    :param admin.ModelAdmin: This class is used to define the admin panel for the AboutSlider model
    :type admin.ModelAdmin: class
    :return
    '''
    list_display = ('photo_hor_src_tag', 'photo_vert_src_tag', 'phrase', 'autor', 'is_visible', 'position')
    list_filter = ('is_visible',)
    list_editable = ('is_visible', 'position')
    search_fields = ('phrase', 'autor')
    ordering = ('position',)

    def photo_hor_src_tag(self, obj):

        if obj.photo_hor:
            return mark_safe(f'<img src="{obj.photo_hor.url}" width=50 height=50>')

    photo_hor_src_tag.short_description = 'Photo Horizontal'

    def photo_vert_src_tag(self, obj):

        if obj.photo_vert:
            return mark_safe(f'<img src="{obj.photo_vert.url}" width=50 height=50>')

    photo_vert_src_tag.short_description = 'Photo Vertical'


@admin.register(AboutRestaurant)
class AboutRestaurantAdmin(admin.ModelAdmin):
    '''
    This class is used to define the admin panel for the AboutRestaurant model
    :param admin.ModelAdmin: This class is used to define the admin panel for the AboutRestaurant model
    :type admin.ModelAdmin: class
    :return
    '''
    list_display = ('title', 'phrase', 'photo_chef_src_tag', 'is_visible', 'position', 'mark', 'autor_mark', 'authentic_phrase')
    list_filter = ('is_visible',)
    list_editable = ('is_visible', 'position', 'mark', 'autor_mark', 'authentic_phrase')
    search_fields = ('title', 'phrase')
    ordering = ('position',)

    def photo_chef_src_tag(self, obj):

        if obj.photo_chef:
            return mark_safe(f'<img src="{obj.photo_chef.url}" width=50 height=50>')

    photo_chef_src_tag.short_description = 'Chef Photo'


@admin.register(AboutSpecial)
class AboutSpacialAdmin(admin.ModelAdmin):
    '''
    This class is used to define the admin panel for the AboutSpecial model
    :param admin.ModelAdmin: This class is used to define the admin panel for the AboutSpecial model
    :type admin.ModelAdmin: class
    :return
    '''
    list_display = ('position','title', 'phrase', 'photo_src_tag', 'is_visible')
    list_filter = ('is_visible',)
    list_editable = ('is_visible','title', 'phrase')
    search_fields = ('title', )
    ordering = ('position',)

    def photo_src_tag(self, obj):

        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width=50 height=50>')

    photo_src_tag.short_description = 'Photo'

@admin.register(AboutAwards)
class AboutAwardsAdmin(admin.ModelAdmin):
    '''
    This class is used to define the admin panel for the AboutAwards model
    :param admin.ModelAdmin: This class is used to define the admin panel for the AboutAwards model
    :type admin.ModelAdmin: class
    :return
    '''
    list_display = ( 'logo_src_tag', 'position', 'title', 'year', 'is_visible')
    list_filter = ('is_visible',)
    list_editable = ('is_visible', 'position', 'title', 'year')
    ordering = ('position',)

    def logo_src_tag(self, obj):

        if obj.logo:
            return mark_safe(f'<img src="{obj.logo.url}" width=50 height=50>')

    logo_src_tag.short_description = 'Awards Logo'


@admin.register(AboutBottomSlider)
class AboutBottomSliderAdmin(admin.ModelAdmin):
    '''
    This class is used to define the admin panel for the AboutBottomSlider model
    :param admin.ModelAdmin: This class is used to define the admin panel for the AboutBottomSlider model
    :type admin.ModelAdmin: class
    :return
    '''
    list_display = ('photo_src_tag', 'title', 'phrase', 'is_visible', 'position')
    list_filter = ('is_visible',)
    list_editable = ('is_visible', 'position', 'title', 'phrase')
    ordering = ('position',)

    def photo_src_tag(self, obj):

        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width=50 height=50>')

    photo_src_tag.short_description = 'Photo'