import fitz

from app.schemas.layout import TextBlock


class PDFParser:

    @staticmethod
    def extract_layout(pdf_path: str):

        document = fitz.open(pdf_path)

        pages = []

        for page_number, page in enumerate(document, start=1):

            page_blocks = []

            blocks = page.get_text("blocks")

            blocks = sorted(
                blocks,
                key=lambda b: (round(b[1], 1), round(b[0], 1))
            )

            for block in blocks:

                x0, y0, x1, y1, text, *_ = block

                text = text.strip()

                if not text:
                    continue

                page_blocks.append(
                    TextBlock(
                        x0=x0,
                        y0=y0,
                        x1=x1,
                        y1=y1,
                        text=text
                    ).model_dump()
                )

            pages.append(
                {
                    "page": page_number,
                    "blocks": page_blocks
                }
            )

        document.close()

        return {
            "total_pages": len(pages),
            "pages": pages
        }
