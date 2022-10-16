
# from unittest import skip

from django.urls import resolve, reverse
from recipes import views

from .test_recipe_base import RecipeTestBase


class RecipesCategoryViewsTest(RecipeTestBase):
    def test_recipe_category_view_function_is_correct(self):
        view = resolve(reverse('recipes:category', args=(1,)))
        self.assertIs(view.func, views.category)

    def test_recipe_category_view_returns_404_if_no_recipes_found(self):
        response = self.client.get(reverse('recipes:category', args=(1000,)))
        self.assertEqual(response.status_code, 404)

    def test_recipe_category_template_loads_recipes(self):
        # This test needs a recipe, hence the 'make_recipe' below
        self.make_recipe(title='This is a category test')
        response = self.client.get(reverse('recipes:category', args=(1,)))
        content = response.content.decode('utf-8')

        # Check some content from the recipe
        self.assertIn('This is a category test', content)
        self.assertIn('10 Minutos', content)
        self.assertIn('5 Porçoes', content)

    def test_if_recipe_category_template_loads_unpublished_recipes(self):
        # This test needs a recipe, hence the 'make_recipe' below
        recipe = self.make_recipe(is_published=False)
        response = self.client.get(
            reverse('recipes:category', args=(recipe.category.id,)))
        self.assertEqual(response.status_code, 404)
