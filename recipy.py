from ingredient import Ingredient


class Recipy:
    def __init__(self, ingredients: list[Ingredient], description: str):
        self.__ingredients = ingredients
        self.__description = description

    def __repr__(self) -> str:
        return f'Ingredients: {self.__ingredients}; Description: {''.join(self.__description)}'
