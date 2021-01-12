import psutil
from pydantic import BaseModel


class Disk(BaseModel):
    device: str
    mountpoint: str
    free_bytes: int
    total_bytes: int
    used_percent: float

    @staticmethod
    def poll(device: str, mountpoint: str) -> 'Disk':
        disk_usage = psutil.disk_usage(mountpoint)

        return Disk(
            device=device,
            mountpoint=mountpoint,
            free_bytes=disk_usage.free,
            total_bytes=disk_usage.total,
            used_percent=disk_usage.percent,
        )
