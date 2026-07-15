from pydantic import BaseModel


class TextBlock(BaseModel):
    x0: float
    y0: float
    x1: float
    y1: float
    text: str


class PageLayout(BaseModel):
    page: int
    blocks: list[TextBlock]


class LayoutResponse(BaseModel):
    total_pages: int
    pages: list[PageLayout]
