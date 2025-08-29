class Ingredient:
    def __init__(self, name: str, quantity: str):
        self.__name = name
        self.__quantity = quantity

    def __str__(self):
        return f"{self.__quantity} {self.__name}"

    def get_name(self):
        return self.__name

    def get_quantity(self):
        return self.__quantity
