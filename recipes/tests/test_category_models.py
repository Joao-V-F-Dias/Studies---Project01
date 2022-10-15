from django.core.exceptions import ValidationError

from .test_recipe_base import RecipeTestBase


class CategoryModelTest(RecipeTestBase):
    def setUp(self) -> None:
        self.category = self.make_category(name='Category Testing')
        return super().setUp()

    def test_category_string_representation(self):
        self.assertEqual(str(self.category), self.category.name)

    def test_category_model_name_max_length_is_65chars(self):
        self.category.name = 'a' * 66
        with self.assertRaises(ValidationError):
            self.category.full_clean()
