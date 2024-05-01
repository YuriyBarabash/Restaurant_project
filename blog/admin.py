from django.contrib import admin
from .models import Blog
from django.utils.safestring import mark_safe


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('mark', 'title', 'is_published', 'created_at', 'photo_src_tag')
    list_filter = ('is_published',)
    search_fields = ('title', )
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)
    list_editable = ('is_published','title')

    def photo_src_tag(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width=50 height=50>')

    photo_src_tag.short_description = 'Photo'
