from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.infrastructure.config.settings import Settings
from app.interfaces.api.routes import router


def create_app() -> FastAPI:
    settings = Settings()

    app = FastAPI(
        title=settings.application_name,
        description=settings.application_description,
        version="1.0.0",
        docs_url="/docs",
        redoc_url="/redoc",
        openapi_url="/openapi.json",
    )

    # No CORS configuration was made in order to make the evaluation easier
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(router, prefix="/api/v1")

    return app


app = create_app()
