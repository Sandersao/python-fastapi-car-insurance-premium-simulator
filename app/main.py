from fastapi import FastAPI
from app.interfaces.api.routes import router
from app.infrastructure.config.settings import Settings

app = FastAPI(title=Settings.application_name)

app.include_router(router)