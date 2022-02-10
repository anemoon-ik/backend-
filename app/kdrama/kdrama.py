from dataclasses import dataclass
from email.mime import image
from uuid import UUID, uuid4

@dataclass
class Kdrama:
    moment: image
    name: str
    year: int
    remembered: str
    id: UUID

