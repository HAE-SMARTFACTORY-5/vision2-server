from fastapi import APIRouter
from service import myIngredientService
from dto import recipy, myIngredient


api = APIRouter()

@api.get("/ingredients")
def getAllIngredients() -> list[myIngredient.MyIngredientResponse]:
    return myIngredientService.findAllMyIngredients()

@api.get("/recipes")
def getAllRecipes() -> list[recipy.RecipyResponse]:
    return myIngredientService.findAllRecipesByMyIngredients()
