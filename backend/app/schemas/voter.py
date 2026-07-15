from typing import Optional

from pydantic import BaseModel


class VoterRecord(BaseModel):
    page: int

    serial_number: Optional[int] = None

    epic_number: Optional[str] = None

    voter_name: Optional[str] = None

    relation_name: Optional[str] = None

    relation_type: Optional[str] = None

    house_number: Optional[str] = None

    age: Optional[int] = None

    gender: Optional[str] = None

    raw_text: str
