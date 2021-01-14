from prometheus_client import Gauge

from instruments.constants import METRICS_PREFIX
from models.cpu import CPU as Model, CPU_PERCENT_INTERVAL


class CPU:
    load: Gauge = Gauge(
        f'{METRICS_PREFIX}_cpu_load',
        'Average CPU load',
        ['interval'],
    )
    percent: Gauge = Gauge(
        f'{METRICS_PREFIX}_cpu_percent',
        f'System wide CPU utilization over {CPU_PERCENT_INTERVAL} seconds [%]',
    )
    temperature: Gauge = Gauge(
        f'{METRICS_PREFIX}_cpu_temperature',
        'CPU temperature [ºC]',
    )

    def __init__(self, model: Model):
        self.load.labels('1').set(model.load_01)
        self.load.labels('5').set(model.load_05)
        self.load.labels('15').set(model.load_15)
        self.percent.set(model.percent)
        self.temperature.set(model.temperature or 'NaN')
