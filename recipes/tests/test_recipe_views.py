from django.urls import reverse, resolve
from recipes import views
from .test_recipe_base import RecipeTestBase
from unittest import skip


class RecipeViewsTest(RecipeTestBase): 
    def test_recipe_home_view_function_is_correct(self):
        view = resolve(reverse('recipes:home'))
        self.assertIs(view.func, views.home)
        
    def test_recipe_home_views_return_status_200_code_OK(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertEqual(response.status_code, 200)

    def test_recipe_home_views_loads_template_is_correct(self):
            response = self.client.get(reverse('recipes:home'))
            self.assertTemplateUsed(response, 'recipes/pages/home.html')
    
    @skip('WIP')
    def test_recipe_home_template_shows_no_recipes_found_if_no_recipes(self):
         response = self.client.get(reverse('recipes:home'))
         self.assertIn(
            'Nada por aqui',
            response.content.decode('utf-8'))

    def test_recipe_home_template_loads_recipe(self):
         # need a recipe for this test
         self.make_recipe(author_data={
              'first_name':'Marcos'
         })
         response = self.client.get(reverse('recipes:home'))
         content = response.content.decode('utf-8')

         #check if one recipes exists
         self.assertIn('Recipe Title', content),


      
    def test_category_view_is_correct(self):
        view = resolve(reverse('recipes:category', kwargs={ 'category_id' : 1}))
        self.assertIs(view.func, views.category)
    
    def test_recipe_category_view_return_404_if_no_recipes_found(self):
        response = self.client.get(reverse('recipes:category', kwargs={ 'category_id' : 1000}))
        self.assertEqual(response.status_code, 404)

    def test_recipes_detail_view_is_correct(self):
        view = resolve(reverse('recipes:recipe', kwargs= { 'id' : 1}))
        self.assertIs(view.func, views.recipe)

    def test_recipe_detail_view_return_404_if_no_recipes_found(self):
        response = self.client.get(reverse('recipes:recipe', kwargs={ 'id' : 1000}))
        self.assertEqual(response.status_code, 404)

