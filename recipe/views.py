from django.shortcuts import render, redirect
from .models import Recipe

# Create your views here.

def recipe_list(request):
    recipe = Recipe.objects.all()
    context = {
        "title" : "Recipe Book",
        "recipes" : recipe
    }
    return render(request, 'list.html', context) 

def create(request):
    if request.method == "POST":
        name = request.POST.get('name')
        ingredient = request.POST.get('ingredient')
        instruction = request.POST.get('instruction')
        time = request.POST.get('time')
        level = request.POST.get('level')
        Recipe.objects.create(name = name, ingredient = ingredient, instruction = instruction, time =  time, level = level)
        return redirect('/recipe/')
    return render(request, "create.html")