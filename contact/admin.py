from django.contrib import admin
from .models import Address, FollowUs


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('street', 'city', 'country')


@admin.register(FollowUs)
class FollowUsAdmin(admin.ModelAdmin):
    list_display = ('mark',)


