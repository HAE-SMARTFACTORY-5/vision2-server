from fastapi import FastAPI
from routes import router

app = FastAPI()
app.include_router(router.api)

if __name__ == '__main__':
    print("run")