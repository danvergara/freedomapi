"""app/main.py"""

from fastapi import FastAPI

from app.api import healthcheck


def create_application() -> FastAPI:
    """Returns an instance of FastAPI with all the settings"""
    application = FastAPI()
    # include the routers
    application.include_router(healthcheck.router)
    return application


app = create_application()
