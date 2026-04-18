from fastapi import FastAPI
from app.interfaces.api.routes import router

app = FastAPI(title="Car Insurance API")

app.include_router(router)