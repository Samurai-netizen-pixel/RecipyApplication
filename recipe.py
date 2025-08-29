from ingredient import Ingredient


class Recipe:
    def __init__(self, name: str, ingredients: list[Ingredient], instructions: str):
        self.__name = name
        self.__ingredients = ingredients
        self.__instructions = instructions

    def __str__(self):
        ingredient_list = "\n ".join(str(ing) for ing in self.__ingredients)
        return (f"Recipe: {self.__name}\n"
                f"Ingredients:\n {ingredient_list}\n"
                f"Instructions:\n{self.__instructions}")

    def has_ingredient(self, ingredient_name: str) -> bool:
        for ingredient in self.__ingredients:

            if ingredient.get_name().lower() == ingredient_name:
                return True

    def get_name(self):
        return self.__name

    def get_ingredients(self):
        return self.__ingredients

    def get_instructions(self):
        return self.__instructions
