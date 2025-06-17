class FileHandler:
    def __init__(self, file_name: str):
        self.__file_name = file_name
        self.__my_file = None

    def write(self, recipies: list[str]):
        with open(self.__file_name, 'w') as self.__my_file:
            self.__my_file.write('\n'.join(recipies))

    def read(self) -> str:
        try:
            with open(self.__file_name, 'r') as self.__my_file:
                return self.__my_file.read()
        except:
            return ''
