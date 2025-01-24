from fastapi import FastAPI
from routes import routes

app = FastAPI()
app.include_router(routes.api)

if __name__ == '__main__':
    print("run")