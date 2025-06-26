class ApplicationOperations:
    def input_recipy_id(self):
        self.__recipy_id = input('Придумайте уникальный номер для рецепта: ').lower().strip()
        return self.__recipy_id

    def input_ingredients(self, ingredient_count):
        self.__ingredients = []

        for self.__ingredient in range(ingredient_count):
            self.__new_ingredient = input('Введите название ингредиента: ').lower().strip()

            if len(self.__new_ingredient) == 0:
                print('Недостаточно информации')
            else:
                self.__ingredients.append(self.__new_ingredient)
        return self.__ingredients

    def input_description(self):
        self.__description = input('Введите описание рецепта: ').strip()
        return self.__description

    def input_and_check_count_of_ingredients(self):
        self.__correct_answer = False

        while self.__correct_answer != True:
            self.__ingredient_count = input('Введите количество ингридиентов: ')

            try:
                self.__ingredient_count = int(self.__ingredient_count)

                if self.__ingredient_count > 0:
                    self.__correct_answer = True
                else:
                    print('Некорректное число')
            except:
                print('Неверный тип данных')

        return self.__ingredient_count
