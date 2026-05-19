from django.urls import path
from .views import recipe_list
from .views import create

urlpatterns = [
    path('recipe/', recipe_list),
    path('recipe/create/', create)
]
