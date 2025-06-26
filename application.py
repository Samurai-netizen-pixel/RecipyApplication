from application_operations_for_working_with_recepies import ApplicationOperations
from application_view import ApplicationView
from file_handler import FileHandler
from user import User


class Application:
    def __init__(self, file_name: str):
        self.__user = User()
        self.__file_handler = FileHandler(file_name)
        self.__application_view = ApplicationView()
        self.__application_operations = ApplicationOperations()

    def try_get_info_from_file(self):
        try:
            self.__recipies_info = self.__file_handler.read()
            self.__recipies_list_info = self.__recipies_info.split('\n')

            for recipy_info in self.__recipies_list_info:
                self.__first_splitter_index = recipy_info.find(': ')
                self.__second_splitter_index = recipy_info.find(';')
                self.__third_splitter_index = recipy_info.find('ID: ')
                self.__fourth_splitter_index = recipy_info.rfind(';')
                self.__fifth_splitter_index = recipy_info.rfind(': ')

                self.__ingredients_info = list(
                    recipy_info[self.__first_splitter_index + 1: self.__second_splitter_index].strip())
                self.__id_info = recipy_info[self.__third_splitter_index + 4: self.__fourth_splitter_index].strip()
                self.__description = recipy_info[self.__fifth_splitter_index + 2:]
                self.__user.create_recipy(self.__ingredients_info, self.__id_info, self.__description)

        except:
            return ''

    def run(self):
        is_running = True

        while is_running:
            self.__application_view.show_menu()
            command = input().lower().strip()

            match command:
                case '1':
                    recipy_id = self.__application_operations.input_recipy_id()
                    ingredient_count = self.__application_operations.input_and_check_count_of_ingredients()
                    ingredients = self.__application_operations.input_ingredients(ingredient_count)
                    description = self.__application_operations.input_description()

                    self.__application_view.show_loading()

                    self.__user.create_recipy(ingredients, recipy_id, description)

                case '2':
                    recipy_id = self.__application_operations.input_recipy_id()

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
