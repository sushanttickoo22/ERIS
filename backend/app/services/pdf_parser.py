import fitz


class PDFParser:

    @staticmethod
    def extract_text(pdf_path: str):

        document = fitz.open(pdf_path)

        full_text = []

        for page in document:
            full_text.append(page.get_text())

        document.close()

        text = "\n".join(full_text)

        return {
            "pages": len(full_text),
            "characters": len(text),
            "preview": text[:2000],
            "text": text,
        }
