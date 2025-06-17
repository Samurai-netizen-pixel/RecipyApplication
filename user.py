from database import Database
from recipy_creator import RecipyCreator


class User:
    def __init__(self):
        self.__recipy_creator = RecipyCreator()
        self.__recipies = Database()

    def create_recipy(self, ingredients: list[str], id: str):
        if ingredients is None:
            raise ValueError('Отсутствие ингредиентов при добавлении рецепта пользователю')

        success_message = 'Успешно!'

        if len(self.__recipies.__repr__()) > 0:
            for recipy in self.__recipies.__repr__():
                if recipy.get_id() == id:
                    print('Такой рецепт уже есть')
                    break
                else:
                    recipy = self.__recipy_creator.create(ingredients, id)
                    self.__recipies.add(recipy)
                    print(success_message)
        else:
            recipy = self.__recipy_creator.create(ingredients, id)
            self.__recipies.add(recipy)
            print(success_message)

    def remove_recipy(self, id: str):
        for recipy in self.__recipies.__repr__():
            if recipy.get_id() == id:
                self.__recipies.remove(recipy)

    def get_recipies(self) -> list:
        return self.__recipies.get_recipies()

    def get_recipies_info(self):
        recipies_info = []

        for recipy in self.get_recipies():
            recipies_info.append(recipy.__repr__())

        return recipies_info

