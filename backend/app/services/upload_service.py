import os
import uuid

from fastapi import UploadFile
from sqlalchemy.orm import Session

from app.core.config import settings
from app.repositories.upload_repository import UploadRepository

UPLOAD_DIR = settings.UPLOAD_FOLDER
os.makedirs(UPLOAD_DIR, exist_ok=True)


class UploadService:

    @staticmethod
    async def save(
        db: Session,
        file: UploadFile,
    ):

        if not file.filename.lower().endswith(".pdf"):
            raise ValueError("Only PDF files are allowed.")

        extension = os.path.splitext(file.filename)[1]
        filename = f"{uuid.uuid4()}{extension}"

        filepath = os.path.join(UPLOAD_DIR, filename)

        with open(filepath, "wb") as f:
            f.write(await file.read())

        repository = UploadRepository(db)

        record = repository.create(
            filename=filename,
            original_filename=file.filename,
            file_type=file.content_type,
        )

        return record
