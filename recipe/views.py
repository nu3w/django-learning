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

def update(request, id):
    recipe = Recipe.objects.get(id = id)
    context = {"recipe" : recipe}
    if request.method == "POST":
        name = request.POST.get("name")
        ingredient = request.POST.get("ingredient")
        instruction = request.POST.get("instruction")
        time = request.POST.get("time")
        level = request.POST.get("level")
        recipe.name = name
        recipe.ingredient = ingredient
        recipe.instruction = instruction
        recipe.time = time
        recipe.level = level
        recipe.save()
        return redirect('/recipe/')
    return render(request, "update.html", context)

def delete(request, id):
    recipe = Recipe.objects.get(id = id)
    recipe.delete()
    return redirect('/recipe/')