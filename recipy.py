class Recipy:
    def __init__(self, ingredients: list[str], description: str):
        if len(ingredients) == 0:
            raise ValueError('Попытка создать рецепт с отсутствующими ингридиентами')

        self.__ingredients = ingredients
        self.__description = description

    def __repr__(self) -> str:
        return f'Recipy: {' '.join(self.__ingredients)}; Description: {''.join(self.__description)}'
