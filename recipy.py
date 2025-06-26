class Recipy:
    def __init__(self, ingredients: list[str], id: str, description: str):
        if len(ingredients) == 0:
            raise ValueError('Попытка создать рецепт с отсутствующими ингридиентами')

        self.__ingredients = ingredients
        self.__id = id
        self.__description = description

    def __repr__(self) -> str:
        return f'Recipy: {' '.join(self.__ingredients)}; ID: {''.join(self.__id)}; Description: {''.join(self.__description)}'

    def __str__(self) -> str:
        return f'{' '.join(self.__ingredients), {' '.join(self.__id)}}'

    def get_id(self) -> str:
        return self.__id
