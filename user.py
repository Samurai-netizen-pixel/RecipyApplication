from database import Database
from recipy_creator import RecipyCreator


class User:
    def __init__(self):
        self.__recipy_creator = RecipyCreator()
        self.__recipies = Database()

    def create_recipy(self, ingredients: list[str], description: str):
        if ingredients is None:
            raise ValueError('Отсутствие ингредиентов при добавлении рецепта пользователю')

        recipy = self.__recipy_creator.create(ingredients, description)
        self.__recipies.add(recipy)
        return recipy

    def remove_recipy(self, selected: int):
        for recipy in self.get_recipies():
            if self.get_recipies().index(recipy) == selected:
                self.__recipies.remove(recipy)
                break

    def get_recipies(self) -> list:
        return self.__recipies.get_recipies()

    def get_recipies_info(self):
        recipies_info = []

        for recipy in self.get_recipies():
            recipies_info.append(recipy.__repr__())

        return recipies_info
