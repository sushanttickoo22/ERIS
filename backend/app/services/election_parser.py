import re


class ElectionParser:
    """
    Utility class for identifying pages that contain voter data.
    """

    HEADER_PATTERNS = [
        r"EPIC",
        r"Elector Name",
        r"Relation Name",
        r"House No",
        r"Age",
        r"Gender",
        r"Sl\.?\s*No",
    ]

    @staticmethod
    def is_voter_page(text: str) -> bool:
        """
        Returns True if the page appears to contain voter entries.
        """
        score = 0

        for pattern in ElectionParser.HEADER_PATTERNS:
            if re.search(pattern, text, re.IGNORECASE):
                score += 1

        return score >= 3

    @staticmethod
    def clean_text(text: str) -> str:
        """
        Remove excessive whitespace while preserving line breaks.
        """
        lines = []

        for line in text.splitlines():
            line = re.sub(r"\s+", " ", line).strip()

            if line:
                lines.append(line)

        return "\n".join(lines)
