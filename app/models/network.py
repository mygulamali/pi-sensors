from typing import Optional

from pydantic import BaseModel


class Network(BaseModel):
    name: str
    address: Optional[str]
    received_bytes: int
    sent_bytes: int
