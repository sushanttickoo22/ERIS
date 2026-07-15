import os

from fastapi import APIRouter, HTTPException

from app.core.config import settings
from app.services.pdf_parser import PDFParser

router = APIRouter(
    prefix="/parser",
    tags=["Parser"],
)


@router.get("/{filename}")
def parse_pdf(filename: str):

    filepath = os.path.join(
        settings.UPLOAD_FOLDER,
        filename,
    )

    if not os.path.exists(filepath):
        raise HTTPException(
            status_code=404,
            detail="PDF not found.",
        )

    result = PDFParser.extract_text(filepath)

    return {
        "pages": result["pages"],
        "characters": result["characters"],
        "preview": result["preview"],
    }
