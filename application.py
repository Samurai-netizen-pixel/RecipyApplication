from application_view import ApplicationView
from file_handler import FileHandler
from user import User


class Application:
    def __init__(self, file_name: str):
        self.__user = User()
        self.__file_handler = FileHandler(file_name)
        self.__application_view = ApplicationView()

    def try_get_info_from_file(self):
        try:
            self.__recipies_info = self.__file_handler.read()
            self.__recipies_list_info = self.__recipies_info.split('\n')

            for recipy_info in self.__recipies_list_info:
                self.__first_splitter_index = recipy_info.find(': ')
                self.__second_splitter_index = recipy_info.find(';')
                self.__third_splitter_index = recipy_info.rfind(': ')
                self.__ingredients_info = list(
                    recipy_info[self.__first_splitter_index + 1: self.__second_splitter_index].strip())
                self.__id_info = recipy_info[self.__third_splitter_index + 1:].strip()
                self.__user.create_recipy(self.__ingredients_info, self.__id_info)

        except:
            return ''

    def run(self):
        is_running = True

        while is_running:
            self.__application_view.show_menu()
            command = input().lower().strip()

            match command:
                case '1':
                    recipy_id = input('Придумайте уникальный номер для рецепта: ').lower().strip()
                    correct_answer = False

                    while correct_answer != True:
                        ingredient_count = input('Введите количество ингридиентов: ')

                        try:
                            ingredient_count = int(ingredient_count)

                            if ingredient_count > 0:
                                correct_answer = True
                            else:
                                print('Некорректное число')
                        except:
                            print('Неверный тип данных')

                    ingredients = []

                    for ingredient in range(ingredient_count):
                        new_ingredient = input('Введите название ингредиента: ').lower().strip()

                        if len(new_ingredient) == 0:
                            print('Недостаточно информации')
                        else:
                            ingredients.append(new_ingredient)

                    self.__application_view.show_loading()

                    self.__user.create_recipy(ingredients, recipy_id)

                case '2':
                    recipy_id = input('Введите уникальный номер для рецепта: ').lower().strip()

                    self.__application_view.show_loading()

                    self.__user.remove_recipy(recipy_id)
                    print('Успешно!')

                case '3':
                    print(self.__user.get_recipies())

                case '4':
                    recipies = self.__user.get_recipies_info()
                    self.__file_handler.write(recipies)

                case '0':
                    is_running = False

                case _:
                    print('Неверная команда')
