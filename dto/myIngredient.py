class MyIngredientResponse:
    def __init__(self, ingredientId: int, name: str, image: str):
        self.ingredientId = ingredientId
        self.name = name
        self.image = image