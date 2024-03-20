from django.test import TestCase
from django.urls import reverse, resolve
from recipes import views
from recipes.models import Category, Recipe, User


class RecipeViewsTest(TestCase):
    def test_recipe_home_view_function_is_correct(self):
        view = resolve(reverse('recipes:home'))
        self.assertIs(view.func, views.home)
        
    def test_recipe_home_views_return_status_200_code_OK(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertEqual(response.status_code, 200)

    def test_recipe_home_views_loads_template_is_correct(self):
            response = self.client.get(reverse('recipes:home'))
            self.assertTemplateUsed(response, 'recipes/pages/home.html')
    
    def test_recipe_home_template_shows_no_recipes_found_if_no_recipes(self):
         response = self.client.get(reverse('recipes:home'))
         self.assertIn(
            'Nada por aqui',
            response.content.decode('utf-8'))
    
    def test_recipe_home_template_loads_recipe(self):
         category = Category.objects.create(name='Category')
         author = User.objects.create_user(
                first_name = 'user',
                last_name = 'name',
                username = 'username',
                password = '123456',
                email = 'username@email.com',
         )
         recipe = Recipe.objects.create(
            category = category,
            author = author,
            title = 'Recipe Title',
            description = 'Recipe Description',
            slug = 'recipe-slug',
            preparation_time = 10,
            preparation_time_unit = 'Minutes',
            servings = 10,
            servings_unit = 'Porções',
            preparation_steps = 'recipe preparation steps',
            preparation_steps_is_html = False,
            is_published = True,
         )
         response = self.client.get(reverse('recipes:home'))
         content = response.content.decode('utf-8')
         self.assertIn('Recipe Title', content),
         self.assertIn('10 Minutes', content),
         self.assertIn('10 Porções', content)

      
    def test_category_view_is_correct(self):
        view = resolve(reverse('recipes:category', kwargs={ 'category_id' : 1}))
        self.assertIs(view.func, views.category)
    
    def test_recipe_category_view_return_404_if_no_recipes_found(self):
        response = self.client.get(reverse('recipes:category', kwargs={ 'category_id' : 1}))
        self.assertEqual(response.status_code, 404)

    def test_recipes_detail_view_is_correct(self):
        view = resolve(reverse('recipes:recipe', kwargs= { 'id' : 1}))
        self.assertIs(view.func, views.recipe)

    def test_recipe_detail_view_return_404_if_no_recipes_found(self):
        response = self.client.get(reverse('recipes:recipe', kwargs={ 'id' : 1}))
        self.assertEqual(response.status_code, 404)

