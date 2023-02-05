from fastapi import FastAPI
from routers import products, users
from fastapi.staticfiles import StaticFiles

app = FastAPI()

## Routers
app.include_router(products.router)
app.include_router(users.router)
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def root():
    return {"message" : "Hola Mundo"}

## localhost:8000/url

@app.get("/url")
async def url():
    return { "url_youtube": "https://www.youtube.com" }

## Inicia server: python -m uvicorn main:app --reload
## Detener con CTRL + C

## Documentacion Swagger: localhost:8000/docs
## Documentacion Redocly: localhost:8000/redoc
