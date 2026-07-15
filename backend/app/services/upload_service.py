import os
import uuid

from fastapi import UploadFile
from sqlalchemy.orm import Session

from app.core.config import settings
from app.repositories.upload_repository import UploadRepository
from app.utils.file_utils import calculate_sha256

UPLOAD_DIR = settings.UPLOAD_FOLDER
os.makedirs(UPLOAD_DIR, exist_ok=True)


class UploadService:

    @staticmethod
    async def save(db: Session, file: UploadFile):

        if not file.filename.lower().endswith(".pdf"):
            raise ValueError("Only PDF files are allowed.")

        data = await file.read()

        max_size = settings.MAX_UPLOAD_SIZE_MB * 1024 * 1024

        if len(data) > max_size:
            raise ValueError(
                f"Maximum upload size is {settings.MAX_UPLOAD_SIZE_MB} MB."
            )

        sha256 = calculate_sha256(data)

        repo = UploadRepository(db)

        existing = repo.get_by_hash(sha256)

        if existing:
            return existing

        extension = os.path.splitext(file.filename)[1]

        filename = f"{uuid.uuid4()}{extension}"

        filepath = os.path.join(
            UPLOAD_DIR,
            filename,
        )

        with open(filepath, "wb") as f:
            f.write(data)

        return repo.create(
            filename=filename,
            original_filename=file.filename,
            file_type=file.content_type,
            file_size=len(data),
            sha256=sha256,
        )
