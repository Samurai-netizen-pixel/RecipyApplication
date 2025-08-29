from recipe import Recipe


class RecipeViewModel:

    def __init__(self, recipe: Recipe):
        self.__recipe = recipe

    @property
    def display_name(self) -> str:
        return self.__recipe.get_name()

    @property
    def display_ingredients(self) -> str:
        return ", ".join(str(ingredient) for ingredient in self.__recipe.get_ingredients())

    @property
    def display_instructions(self) -> str:
        return self.__recipe.get_instructions()
