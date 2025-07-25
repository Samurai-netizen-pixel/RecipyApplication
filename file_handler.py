class FileHandler:
    def __init__(self, file_name: str):
        self.__file_name = file_name
        self.__my_file = None

    def write_recipies(self, recipies: list[str]):
        with open(self.__file_name, 'w') as self.__my_file:
            self.__my_file.write('\n'.join(recipies))

    def read_recipies(self) -> str:
        try:
            with open(self.__file_name, 'r') as self.__my_file:
                return self.__my_file.read()
        except:
            print(0)

    def write_ingredients(self, ingredients):
        pass
