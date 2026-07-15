import fitz

from app.services.election_parser import ElectionParser


class PDFParser:

    @staticmethod
    def extract_text(pdf_path: str):

        document = fitz.open(pdf_path)

        pages = []

        total_characters = 0

        for index, page in enumerate(document, start=1):

            raw_text = page.get_text("text")

            clean_text = ElectionParser.clean_text(raw_text)

            total_characters += len(clean_text)

            pages.append(
                {
                    "page": index,
                    "is_voter_page": ElectionParser.is_voter_page(clean_text),
                    "characters": len(clean_text),
                    "preview": clean_text[:300],
                    "text": clean_text,
                }
            )

        document.close()

        return {
            "total_pages": len(pages),
            "total_characters": total_characters,
            "pages": pages,
        }
