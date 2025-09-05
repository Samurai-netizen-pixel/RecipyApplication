from ingredient import Ingredient
from recipe import Recipe
from recipe_view_model import RecipeViewModel


class RecipeBookViewModel:
    def __init__(self):
        self.__recipes: list[Recipe] = []
        self.__filtered_recipes: list[Recipe] = []
        self.__current_view_recipes: list[RecipeViewModel] = []

    def add_recipe(self, recipe: Recipe):
        self.__recipes.append(recipe)
        self.update_filtered_recipes()
        self.update_current_view()

    def get_all_recipes(self) -> list[Recipe]:
        return self.__recipes

    def search_by_ingredient(self, ingredient_name: str):
        if not ingredient_name:
            self.__filtered_recipes = self.__recipes
        else:
            self.__filtered_recipes = []

            for recipe in self.__recipes:
                if recipe.has_ingredient(ingredient_name):
                    self.__filtered_recipes.append(recipe)

        self.update_current_view()

    def update_filtered_recipes(self):
        self.__filtered_recipes = self.__recipes

    def update_current_view(self):
        self.__current_view_recipes = [RecipeViewModel(recipe) for recipe in self.__filtered_recipes]

    def get_current_view_recipes(self):
        return self.__current_view_recipes

    def generate_shopping_list(self, selected_recipe_names: list[str]) -> str:
        shopping_list_items = {}
        selected_recipes = [recipe for recipe in self.__recipes if recipe.get_name() in selected_recipe_names]

        for recipe in selected_recipes:
            for ingredient in recipe.get_ingredients():
                item_name = ingredient.get_name().lower()

                if item_name in shopping_list_items:
                    shopping_list_items[item_name] = f"{shopping_list_items[item_name]}, {ingredient.__quantity}"
                else:
                    shopping_list_items[item_name] = ingredient.get_quantity()

            print(shopping_list_items)

            if not shopping_list_items:
                return "No recipes selected for shopping list."

            shopping_list_output = "Shopping List:\n"

            for item, quantity in sorted(shopping_list_items.items()):
                shopping_list_output += f"- {quantity} {item.capitalize()}\n"

            return shopping_list_output

    def load_initial_data(self):
        recipe1 = Recipe(
            name="Scrambled Eggs",
            ingredients=[
                Ingredient("Eggs", "2"),
                Ingredient("Milk", "2 tbsp"),
                Ingredient("Butter", "1 tsp"),
                Ingredient("Salt", "Pinch")
            ],
            instructions="Whisk eggs, milk, and salt. Melt butter in a pan. Pour egg mixture and cook, stirring, until set."
        )
        recipe2 = Recipe(
            name="Tomato Soup",
            ingredients=[
                Ingredient("Canned Tomatoes", "1 can (28 oz)"),
                Ingredient("Vegetable Broth", "4 cups"),
                Ingredient("Onion", "1 medium, chopped"),
                Ingredient("Garlic", "2 cloves, minced"),
                Ingredient("Olive Oil", "1 tbsp"),
                Ingredient("Salt", "to taste"),
                Ingredient("Black Pepper", "to taste")
            ],
            instructions="Sauté onion and garlic in olive oil. Add tomatoes and broth. Simmer for 20 minutes. Blend until smooth. Season with salt and pepper."
        )
        recipe3 = Recipe(
            name="Chicken Salad Sandwich",
            ingredients=[
                Ingredient("Cooked Chicken Breast", "2 cups, shredded"),
                Ingredient("Mayonnaise", "1/2 cup"),
                Ingredient("Celery", "1 stalk, finely chopped"),
                Ingredient("Red Onion", "1/4 cup, finely chopped"),
                Ingredient("Salt", "to taste"),
                Ingredient("Black Pepper", "to taste"),
                Ingredient("Bread", "4 slices")
            ],
            instructions="Combine shredded chicken, mayonnaise, celery, and red onion in a bowl. Season with salt and pepper. Serve on bread."
        )
        self.add_recipe(recipe1)
        self.add_recipe(recipe2)
        self.add_recipe(recipe3)
