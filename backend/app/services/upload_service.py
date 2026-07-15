import os
import uuid

from fastapi import UploadFile

from app.core.config import settings

UPLOAD_DIR = settings.UPLOAD_FOLDER

os.makedirs(
    UPLOAD_DIR,
    exist_ok=True
)


class UploadService:

    @staticmethod
    async def save(file: UploadFile):

        extension = os.path.splitext(file.filename)[1]

        filename = f"{uuid.uuid4()}{extension}"

        filepath = os.path.join(
            UPLOAD_DIR,
            filename
        )

        with open(filepath, "wb") as f:
            f.write(await file.read())

        return filename
