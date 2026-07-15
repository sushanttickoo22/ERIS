import fitz


class PDFParser:
    @staticmethod
    def extract_text(pdf_path: str):
        document = fitz.open(pdf_path)

        pages = []
        total_characters = 0

        for index, page in enumerate(document, start=1):
            text = page.get_text("text")

            characters = len(text)
            total_characters += characters

            pages.append(
                {
                    "page": index,
                    "characters": characters,
                    "preview": text[:500],
                    "text": text,
                }
            )

        document.close()

        return {
            "total_pages": len(pages),
            "total_characters": total_characters,
            "pages": pages,
        }
