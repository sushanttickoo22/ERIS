import os

from fastapi import APIRouter
from fastapi import HTTPException

from app.core.config import settings

from app.services.pdf_parser import PDFParser

router = APIRouter(
    prefix="/parser",
    tags=["Parser"],
)


@router.get("/{filename}")
def parse_pdf(filename: str):

    pdf_path = os.path.join(
        settings.UPLOAD_FOLDER,
        filename,
    )

    if not os.path.exists(pdf_path):

        raise HTTPException(
            status_code=404,
            detail="PDF not found.",
        )

    return PDFParser.extract_layout(pdf_path)
