import itertools
import sys
import time


class ApplicationView:
    def __init__(self):
        self.__done = None
        self.__loading_count = 0
        self.__max_loading_count = 12
        self.__pause_time = 0.3

    def show_loading(self):
        self.__done = False

        for element in itertools.cycle(['.', '..', '...', '....']):

            if self.__done:
                break
            else:
                sys.stdout.write('\rЗагрузка ' + element)
                sys.stdout.flush()
                time.sleep(self.__pause_time)
                self.__loading_count += 1

            if self.__loading_count == self.__max_loading_count:
                self.__done = True
                self.__loading_count = 0

    def show_menu(self):
        print('\n------------------МЕНЮ--------------------')
        print('------------------------------------------')
        print('1 - Добавить рецепт-----------------------')
        print('2 - Удалить рецепт------------------------')
        print('3 - Показать список всех рецептов---------')
        print('4 - Получить отчет в файле----------------')
        print('0 - Выход---------------------------------')
