from django.contrib import admin

from .models import User


class UserAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Личная информация', {'fields': ('first_name', 'last_name')})
    )
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',)
    search_fields = (
        'username',
        'email',
        'first_name',
        'last_name',)
    list_filter = (
        'first_name',
        'email',)
    list_display_links = ('username',)
    empty_value_display = 'Не задано'
    ordering = ('last_name', 'first_name')


admin.site.register(User, UserAdmin)
