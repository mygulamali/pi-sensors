from prometheus_client import Gauge

from instruments.constants import METRICS_PREFIX
from models.memory import Memory as MemoryModel


class Memory:
    available_bytes: Gauge = Gauge(
        f'{METRICS_PREFIX}_memory_available_bytes',
        'Available memory [bytes]',
    )
    total_bytes: Gauge = Gauge(
        f'{METRICS_PREFIX}_memory_total_bytes',
        'Total physical memory [bytes]',
    )
    used_percent: Gauge = Gauge(
        f'{METRICS_PREFIX}_memory_used_percent',
        'Memory used [%]',
    )

    @staticmethod
    def poll() -> None:
        stats = MemoryModel.poll()

        memory = Memory()
        memory.available_bytes.set(stats.available_bytes)
        memory.total_bytes.set(stats.total_bytes)
        memory.used_percent.set(stats.used_percent)
