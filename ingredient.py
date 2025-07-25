class Ingredient:
    def __init__(self, ingredient: str):
        self.__ingredient = ingredient

    def __repr__(self):
        return f'{self.__ingredient}'
