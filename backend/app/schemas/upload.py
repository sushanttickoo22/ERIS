from pydantic import BaseModel


class UploadResponse(BaseModel):

    id: int

    filename: str

    status: str
