from django.contrib import admin
from .models import Category, Dish


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'time_create')
    list_display_links = ('name',)
    search_fields = ('name',)


class DishAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'time_create')
    list_display_links = ('name',)
    search_fields = ('name',)
    list_filter = ('category',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Dish, DishAdmin)
