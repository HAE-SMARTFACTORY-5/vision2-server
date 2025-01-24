from fastapi import APIRouter

api = APIRouter()

@api.get("/hi")
def testHi():
    return 'hi'