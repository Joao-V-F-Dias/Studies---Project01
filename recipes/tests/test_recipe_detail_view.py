
# from unittest import skip

from django.urls import resolve, reverse
from recipes import views

from .test_recipe_base import RecipeTestBase


class RecipeDetailViewsTest(RecipeTestBase):
    def test_recipe_detail_view_function_is_correct(self):
        view = resolve(reverse('recipes:recipe', args=(1,)))
        self.assertIs(view.func, views.recipe)

    # @skip('Skipping this test on purpose')
    def test_recipe_detail_view_returns_404_if_no_recipes_found(self):
        response = self.client.get(reverse('recipes:recipe', args=(1000,)))
        self.assertEqual(response.status_code, 404)

        # Failing this test on purpose
        # self.fail('So I can write more code in it later')

    def test_recipe_detail_template_loads_recipe(self):
        # This test needs a recipe, hence the 'make_recipe' below
        self.make_recipe(title='This is a recipe test')
        response = self.client.get(reverse('recipes:recipe', args=(1,)))
        content = response.content.decode('utf-8')

        # Check some content from the recipe
        self.assertIn('This is a recipe test', content)
        self.assertIn('10 Minutos', content)
        self.assertIn('5 Porçoes', content)

    def test_if_recipe_detail_template_loads_unpublished_recipes(self):
        # This test needs a recipe, hence the 'make_recipe' below
        recipe = self.make_recipe(is_published=False)
        response = self.client.get(
            reverse('recipes:recipe', args=(recipe.id,)))
        self.assertEqual(response.status_code, 404)
