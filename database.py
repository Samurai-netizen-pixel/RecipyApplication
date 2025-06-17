from recipy import Recipy


class Database:
    def __init__(self):
        self.__recipies = []

    def add(self, recipy: Recipy):
        self.__recipies.append(recipy)

    def remove(self, recipy: Recipy):
        self.__recipies.remove(recipy)

    def get_recipies(self) -> list:
        recipies = list(self.__recipies)
        return recipies

    def __repr__(self):
        return list(self.__recipies)
