from pydantic import BaseModel


class PageText(BaseModel):
    page: int
    characters: int
    preview: str


class ParserResponse(BaseModel):
    total_pages: int
    total_characters: int
    pages: list[PageText]
