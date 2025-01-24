import requests
import os
import json
from dotenv import load_dotenv
from fastapi import HTTPException
from dto.recipy import RecipyResponse


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, "../.env"))

def questionToGemini(content):
    URI = os.environ["GEMINI_API_URL"] + "?key=" + os.environ["GEMINI_API_KEY"]
    headers = { "Content-Type": "application/json" }
    data = {
        "contents": [
            {
                "parts": [
                    {"text": buildScript(content)}
                ]
            }
        ]
    }
    try :
        response = requests.post(URI, headers=headers, data=json.dumps(data))
        content = getContent(response)
        recipeData = getRecipeData(content)
        return convertToResponseDto(json.loads(recipeData))

    except requests.ConnectionError as e:
        raise HTTPException(status_code=500, detail=f"Error Gemini API: {e}")

# 프롬프트 스크립트 생성 
def buildScript(ingredients):
    prefix = '다음 재료 중 몇가지 혹은 모두를 가지고 할 수 있는 요리를 내가 제시하는 형식에 맞게 JSON 형태로 알려줘. JSON 이외에 다른 글자들은 작성하지마. 재료에 기타 조미료도 작성하지말고 내가 제시한 자료들만 적어줘. 한국어로 이야기해줘'
    ingredientInput = '= 재료 = \n'
    for ingredient in ingredients:
        ingredientInput = ingredientInput + ', ' + ingredient
    subffix = '''
        = 형식 =
            [

                {

                    "name" : 요리이름,

                    "content" : 요리방법(단계별로),

                    "level" : 난이도(쉬움, 보통, 어려움),

                    "time" : 조리시간,

                    "ingredient": [ 재료들 ]

                }

            ]
        '''
    return prefix + ' \n ' + ingredientInput + ' \n ' + subffix

# response -> content
def getContent(response):
    return response.json()['candidates'][0]['content']['parts'][0]['text']

# content 안에 있는 레시피 정보 추출
def getRecipeData(content):
    return content.replace('json\n', "").replace('\n\n"', "").replace("```", "")

# Response 형식에 맞는 Dto로 전환
def convertToResponseDto(response):
    result = []
    for recipe in response:
        result.append(
            RecipyResponse (
                name = recipe['name'],
                content = recipe['content'],
                level = recipe['level'],
                time = recipe['time'],
                ingredient = recipe['ingredient']
            )
        )
    return result