import re

from app.schemas.voter import VoterRecord


class VoterExtractor:

    EPIC_PATTERN = re.compile(r"[A-Z]{2,3}[0-9]{7,10}")

    AGE_PATTERN = re.compile(r"\b([1-9][0-9]?)\b")

    HOUSE_PATTERN = re.compile(r"\d+\-\d+")

    @staticmethod
    def split_lines(page_text: str):

        lines = []

        for line in page_text.split("\n"):

            line = line.strip()

            if line:

                lines.append(line)

        return lines

    @classmethod
    def extract_records(cls, page: int, page_text: str):

        lines = cls.split_lines(page_text)

        records = []

        for line in lines:

            epic = None

            age = None

            house = None

            serial = None

            epic_match = cls.EPIC_PATTERN.search(line)

            if epic_match:
                epic = epic_match.group()

            age_match = cls.AGE_PATTERN.search(line)

            if age_match:
                age = int(age_match.group())

            house_match = cls.HOUSE_PATTERN.search(line)

            if house_match:
                house = house_match.group()

            serial_match = re.match(r"^\d+", line)

            if serial_match:
                serial = int(serial_match.group())

            records.append(
                VoterRecord(
                    page=page,
                    serial_number=serial,
                    epic_number=epic,
                    house_number=house,
                    age=age,
                    raw_text=line,
                )
            )

        return records
