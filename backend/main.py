from fastapi import FastAPI
from core.config import settings

app = FastAPI(title=settings.PROJECT_VERSION, version=settings.PROJECT_VERSION)


@app.get("/")
def hello_api():
    return{"detail":"hello world"}