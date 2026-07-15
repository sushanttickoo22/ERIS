from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from datetime import datetime

from app.db.base import Base


class UploadedFile(Base):

    __tablename__ = "uploaded_files"

    id = Column(Integer, primary_key=True)

    filename = Column(String, nullable=False)

    original_filename = Column(String, nullable=False)

    file_type = Column(String)

    uploaded_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    status = Column(
        String,
        default="UPLOADED"
    )
