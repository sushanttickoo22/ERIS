from sqlalchemy.orm import Session

from app.models.uploaded_file import UploadedFile


class UploadRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(
        self,
        filename: str,
        original_filename: str,
        file_type: str,
    ) -> UploadedFile:

        record = UploadedFile(
            filename=filename,
            original_filename=original_filename,
            file_type=file_type,
            status="UPLOADED",
        )

        self.db.add(record)
        self.db.commit()
        self.db.refresh(record)

        return record
