from django.contrib import admin
from .models import WordsBelt


@admin.register(WordsBelt)
class WordsBeltAdmin(admin.ModelAdmin):
    list_display = ('position', 'word', 'is_visible')
    list_editable = ('word', 'is_visible')


