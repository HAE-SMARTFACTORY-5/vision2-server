from pydantic import BaseModel

class RecipyResponse(BaseModel):
    name: str
    content: list
    level: str
    time: str
    ingredient: list