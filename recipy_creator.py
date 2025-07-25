from ingredient import Ingredient
from recipy import Recipy


class RecipyCreator:
    def create(self, ingredients: list[Ingredient], description: str) -> Recipy:
        return Recipy(ingredients, description)
