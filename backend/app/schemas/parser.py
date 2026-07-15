from pydantic import BaseModel


class ParseResponse(BaseModel):
    pages: int
    characters: int
    preview: str
