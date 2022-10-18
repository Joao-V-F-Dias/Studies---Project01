

from decouple import config
from django.db.models import Q
from django.http import Http404
from django.shortcuts import get_list_or_404, get_object_or_404, render
from utils.pagination import make_pagination
from utils.recipes.factory import make_recipe

from recipes.models import Recipe

PER_PAGE = config('PER_PAGE', cast=int)


def home(request):
    recipe = Recipe.objects.filter(is_published=True).order_by('-id')

    page_obj, pagination_range = make_pagination(request, recipe, PER_PAGE)

    return render(request, 'recipes/pages/home.html',
                  context={'recipes': page_obj,
                           'pagination_range': pagination_range, })


def category(request, category_id):
    recipe = get_list_or_404(
        Recipe.objects.filter(
            category__id=category_id, is_published=True).order_by('-id'))

    page_obj, pagination_range = make_pagination(request, recipe, PER_PAGE)

    return render(request, 'recipes/pages/category.html',
                  context={'recipes': page_obj,
                           'title': f'{recipe[0].category.name} | Category',
                           'pagination_range': pagination_range, })


def recipe(request, id):
    recipe = get_object_or_404(Recipe, id=id, is_published=True)
    return render(request, 'recipes/pages/recipe-view.html', context={'recipe': recipe, 'is_detail_page': True})


def search(request):
    search_term = request.GET.get('q', '').strip()

    if not search_term:
        raise Http404()

    recipe = Recipe.objects.filter(
        Q(
            Q(title__icontains=search_term) |
            Q(description__icontains=search_term),
        ),
        is_published=True,
    ).order_by('-id')

    page_obj, pagination_range = make_pagination(request, recipe, PER_PAGE)

    return render(request, 'recipes/pages/search.html', context={
        'page_title': f'Search for "{search_term}"',
        'search_term': search_term,
        'recipes': page_obj,
        'pagination_range': pagination_range,
        'additional_url_query': f'&q={search_term}'
    })
