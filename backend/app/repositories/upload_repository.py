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
        file_size: int,
        sha256: str,
    ):
        record = UploadedFile(
            filename=filename,
            original_filename=original_filename,
            file_type=file_type,
            file_size=file_size,
            sha256=sha256,
            status="UPLOADED",
        )

        self.db.add(record)
        self.db.commit()
        self.db.refresh(record)

        return record

    def get_by_hash(self, sha256: str):
        return (
            self.db.query(UploadedFile)
            .filter(UploadedFile.sha256 == sha256)
            .first()
        )
