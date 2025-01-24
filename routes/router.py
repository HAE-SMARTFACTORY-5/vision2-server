from fastapi import APIRouter
from service import myIngredientService


api = APIRouter()

@api.get("/ingredient")
def getAllIngredient():
    return myIngredientService.findAllMyIngredient()
