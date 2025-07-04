from recipy import Recipy


class RecipyCreator:
    def create(self, ingredients: list[str], description: str) -> Recipy:
        return Recipy(ingredients, description)
