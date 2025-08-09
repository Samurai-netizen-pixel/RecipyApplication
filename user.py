from database import Database
from ingredient import Ingredient
from ingredient_creator import IngredientCreator
from recipy_creator import RecipyCreator


class User:
    def __init__(self):
        self.__recipy_creator = RecipyCreator()
        self.__ingredient_creator = IngredientCreator()
        self.__database = Database()

    def create_recipy(self, ingredients: list[Ingredient], description: str):
        if ingredients is None:
            raise ValueError('Отсутствие ингредиентов при добавлении рецепта пользователю')

        recipy = self.__recipy_creator.create(ingredients, description)
        self.__database.add_recipy(recipy)
        return recipy

    def remove_recipy(self, selected_recipy_index: int):
        for recipy in self.get_recipies():
            if self.get_recipies().index(recipy) == selected_recipy_index:
                self.__database.remove_recipy(recipy)
                break

    def get_recipies(self) -> list:
        return self.__database.get_recipies()

    def get_recipies_info(self):
        return self.__database.get_recipies_info()

    def create_ingredient(self, ingredient: str):
        ingredient = self.__ingredient_creator.create(ingredient)
        return ingredient
