
from django.shortcuts import render
from utils.recipes.factory import make_recipe

from recipes.models import Recipe


def home(request):
    recipe = Recipe.objects.filter(is_published=True).order_by('-id')
    return render(request, 'recipes/pages/home.html', context={'recipes': recipe})


def category(request, category_id):
    recipe = Recipe.objects.filter(
        category__id=category_id, is_published=True).order_by('-id')
    return render(request, 'recipes/pages/category.html', context={'recipes': recipe})


def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html', context={'recipe': make_recipe(), 'is_detail_page': True})
