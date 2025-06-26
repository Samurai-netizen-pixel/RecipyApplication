from recipy import Recipy


class RecipyCreator:
    def create(self, ingredients: list[str], id: str, description: str) -> Recipy:
        return Recipy(ingredients, id, description)
