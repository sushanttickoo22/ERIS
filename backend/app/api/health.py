from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
def health():

    return {
        "status": "healthy",
        "application": "ERIS",
        "version": "0.1.0",
    }
