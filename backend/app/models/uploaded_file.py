from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String

from app.db.base import Base


class UploadedFile(Base):
    __tablename__ = "uploaded_files"

    id = Column(Integer, primary_key=True)

    filename = Column(String, nullable=False)

    original_filename = Column(String, nullable=False)

    file_type = Column(String)

    file_size = Column(Integer)

    sha256 = Column(String, unique=True)

    status = Column(String, default="UPLOADED")

    uploaded_at = Column(DateTime, default=datetime.utcnow)
