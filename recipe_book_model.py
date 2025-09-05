from recipe import Recipe


class RecipeBookModel:
    def __init__(self):
        self.__recipes: list[Recipe] = []

    def add_recipe(self, recipe: Recipe):
        self.__recipes.append(recipe)

    def get_all_recipes(self) -> list[Recipe]:
        recipes = list(self.__recipes)
        return recipes

