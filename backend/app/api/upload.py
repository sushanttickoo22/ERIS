from fastapi import APIRouter, Depends, File, HTTPException, UploadFile
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.services.upload_service import UploadService

router = APIRouter(
    prefix="/upload",
    tags=["Upload"],
)


@router.post("/")
async def upload_pdf(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
):
    try:
        record = await UploadService.save(
            db=db,
            file=file,
        )

        return {
            "file_id": record.id,
            "filename": record.filename,
            "original_filename": record.original_filename,
            "status": record.status,
        }

    except ValueError as ex:
        raise HTTPException(
            status_code=400,
            detail=str(ex),
        )
