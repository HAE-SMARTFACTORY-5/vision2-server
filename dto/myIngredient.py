from pydantic import BaseModel

class MyIngredientResponse(BaseModel):
    ingredientId: int
    name: str
    image: str