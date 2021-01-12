import psutil
from pydantic import BaseModel


class Memory(BaseModel):
    available_bytes: int
    total_bytes: int
    used_percent: float

    @staticmethod
    def poll() -> 'Memory':
        memory = psutil.virtual_memory()

        return Memory(
            available_bytes=memory.available,
            total_bytes=memory.total,
            used_percent=memory.percent,
        )
