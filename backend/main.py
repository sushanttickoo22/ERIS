from fastapi import FastAPI

from app.api.health import router as health_router
from app.api.upload import router as upload_router

from app.core.config import settings
from app.core.logging import configure_logging

# Configure logging
configure_logging()

# Create FastAPI application
app = FastAPI(
    title=settings.APP_NAME,
    version="0.1.0",
    description="Election Roll Intelligence System (ERIS) API",
)

# Register API routers
app.include_router(health_router)
app.include_router(upload_router)


@app.get("/", tags=["Root"])
def root():
    return {
        "message": "Welcome to ERIS",
        "application": settings.APP_NAME,
        "version": "0.1.0",
        "status": "running"
    }
