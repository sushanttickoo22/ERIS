from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File

from app.services.upload_service import UploadService

router = APIRouter(
    prefix="/upload",
    tags=["Upload"]
)


@router.post("/")
async def upload_pdf(
    file: UploadFile = File(...)
):

    filename = await UploadService.save(
        file
    )

    return {
        "filename": filename,
        "status": "uploaded"
    }
