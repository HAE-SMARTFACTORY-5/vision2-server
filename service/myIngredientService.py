from repository import myIngredientRepository
from infra import gemini

def findAllMyIngredients():
    return myIngredientRepository.findAll()

def findAllRecipesByMyIngredients():
    myIngredients = myIngredientRepository.findAll()
    myIngredientNames = []
    for myIngredient in myIngredients:
        myIngredientNames.append(myIngredient.name)
    return gemini.questionToGemini(myIngredientNames)