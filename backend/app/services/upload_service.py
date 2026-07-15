import os
import uuid

from fastapi import UploadFile

UPLOAD_DIR = "uploads"

os.makedirs(
    UPLOAD_DIR,
    exist_ok=True
)


class UploadService:

    @staticmethod
    async def save(
        file: UploadFile,
    ):

        extension = os.path.splitext(
            file.filename
        )[1]

        filename = (
            str(uuid.uuid4())
            + extension
        )

        filepath = os.path.join(
            UPLOAD_DIR,
            filename
        )

        with open(
            filepath,
            "wb"
        ) as f:

            f.write(
                await file.read()
            )

        return filename
