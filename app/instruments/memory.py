from prometheus_client import Gauge

from instruments.constants import METRICS_PREFIX
from models.memory import Memory as Model


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

    def __init__(self, model: Model):
        self.available_bytes.set(model.available_bytes)
        self.total_bytes.set(model.total_bytes)
        self.used_percent.set(model.used_percent)
