from prometheus_client import Gauge

from instruments.constants import METRICS_PREFIX
from models.cpu import CPU as CPUModel, CPU_PERCENT_INTERVAL


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

    @staticmethod
    def poll() -> None:
        stats = CPUModel.poll()

        cpu = CPU()
        cpu.load.labels('1').set(stats.load_01)
        cpu.load.labels('5').set(stats.load_05)
        cpu.load.labels('15').set(stats.load_15)
        cpu.percent.set(stats.percent)
        cpu.temperature.set(stats.temperature or 'NaN')
