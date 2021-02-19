from prometheus_client import Gauge

from instruments.constants import METRICS_PREFIX
from models.bme280 import BME280 as Model


class BME280:
    humidity: Gauge = Gauge(
        f"{METRICS_PREFIX}_bme280_humidity",
        "Humidity [%]",
    )
    pressure: Gauge = Gauge(
        f"{METRICS_PREFIX}_bme280_pressure",
        "Barometric pressure [hPa]",
    )
    temperature: Gauge = Gauge(
        f"{METRICS_PREFIX}_bme280_temperature",
        "Ambient temperature [ºC]",
    )

    def __init__(self, model: Model):
        self.humidity.set(model.humidity)
        self.pressure.set(model.pressure)
        self.temperature.set(model.temperature)
