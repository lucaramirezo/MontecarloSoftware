import uuid
from typing import Optional


class ListType:
    UUID: uuid.UUID
    title: str
    details: Optional[str]

    def __init__(self, title: str, details: str = None, uuidv4: Optional[uuid.UUID] = None):
        self.UUID = uuidv4 or uuid.uuid4()
        self.title = title
        self.details = details

    def __str__(self):
        return f"UUID: {self.UUID}, title: {self.title}, details: {self.details}"

    def __lt__(self, other):
        return self.UUID < other.UUID

