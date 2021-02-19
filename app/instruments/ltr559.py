from prometheus_client import Gauge

from instruments.constants import METRICS_PREFIX
from models.ltr559 import LTR559 as Model


class LTR559:
    lux: Gauge = Gauge(
        f'{METRICS_PREFIX}_ltr559_lux',
        'Ambient light [Lux]'
    )
    proximity: Gauge = Gauge(
        f'{METRICS_PREFIX}_ltr559_proximity',
        'Proximity'
    )

    def __init__(self, model: Model):
        self.lux.set(model.lux)
        self.proximity.set(model.proximity)
