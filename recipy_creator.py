from recipy import Recipy


class RecipyCreator:
    def create(self, ingredients: list[str], id: str) -> Recipy:
        return Recipy(ingredients, id)
