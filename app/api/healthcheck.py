"""
app/api/healthcheck.py
"""

from fastapi import APIRouter, Depends

from app.config import get_settings, Settings

router = APIRouter()


@router.get("/healthcheck")
async def healthcheck(settings: Settings = Depends(get_settings)):
    """/healthcheck endpoint"""
    return {
        "message": "ok",
        "environment": settings.environment,
        "testing": settings.testing,
    }
