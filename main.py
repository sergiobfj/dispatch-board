from fastapi import FastAPI
from database import create_db
from routers.orders import router

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db()

app.include_router(router)