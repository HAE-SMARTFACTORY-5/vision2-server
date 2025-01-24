from fastapi import FastAPI
from routes import router

app = FastAPI(docs_url='/api/docs')
app.include_router(router.api)

if __name__ == '__main__':
    print("run")