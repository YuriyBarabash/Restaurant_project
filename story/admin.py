from django.contrib import admin
from .models import StoryContent, StoryPhotos
from django.utils.safestring import mark_safe


@admin.register(StoryContent)
class StoryContentAdmin(admin.ModelAdmin):
    list_display = ('slogan', 'phrase', 'is_visible',)
    list_editable = ('phrase','is_visible',)


@admin.register(StoryPhotos)
class StoryPhotosAdmin(admin.ModelAdmin):
    list_display = ('image_src_tag', 'position',  'is_visible',)
    list_editable = ('is_visible', 'position',)

    def image_src_tag(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width=50 height=50>')

    image_src_tag.short_description = 'Photo'
