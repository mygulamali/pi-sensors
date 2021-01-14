from prometheus_client import Gauge

from instruments.constants import METRICS_PREFIX
from models.disk import Disk as Model


class Disk:
    free_bytes: Gauge = Gauge(
        f'{METRICS_PREFIX}_disk_free_bytes',
        'Free disk space [bytes]',
        ['device', 'mountpoint'],
    )
    total_bytes: Gauge = Gauge(
        f'{METRICS_PREFIX}_disk_total_bytes',
        'Total disk space [bytes]',
        ['device', 'mountpoint'],
    )
    used_percent: Gauge = Gauge(
        f'{METRICS_PREFIX}_disk_used_percent',
        'Used disk space [%]',
        ['device', 'mountpoint'],
    )

    def __init__(self, model: Model):
        labels = {
            'device': model.device,
            'mountpoint': model.mountpoint,
        }

        self.free_bytes.labels(**labels).set(model.free_bytes)
        self.total_bytes.labels(**labels).set(model.total_bytes)
        self.used_percent.labels(**labels).set(model.used_percent)
