from ingredient import Ingredient
from recipy import Recipy


class Database:
    def __init__(self):
        self.__recipies = []

    def add_recipy(self, recipy: Recipy):
        self.__recipies.append(recipy)

    def remove_recipy(self, selected: Recipy):
        self.__recipies.remove(selected)

    def get_recipies(self) -> list:
        recipies = list(self.__recipies)
        return recipies

    def get_recipies_info(self):
        recipies = map(str, self.__recipies)
        return recipies

    def __repr__(self):
        return f'{self.__recipies}'
