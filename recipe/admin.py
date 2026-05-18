from django.contrib import admin
from.models import Recipe

# Register your models here.

# @admin.register(Recipe)

class RecipeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'time', 'ingredient']
    list_filter = ['time']
    search_fields = ['name', 'ingredient', 'time']
    list_per_page = 10
    
admin.site.register(Recipe, RecipeAdmin)