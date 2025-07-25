from ingredient import Ingredient


class IngredientCreator:
    def create(self, ingredient: str):
        return Ingredient(ingredient)
