from django.urls import path
from .views import recipe_list, create, update, delete

urlpatterns = [
    path('recipe/', recipe_list),
    path('recipe/create/', create),
    path('recipe/<id>/', update),
    path('delete/<int:id>/', delete, name="delete")
]
