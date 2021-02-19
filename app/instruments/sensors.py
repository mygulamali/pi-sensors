try:
    from bme280 import BME280 as BME280Sensor
    from ltr559 import LTR559 as LTR559Sensor
except ImportError:
    from mocks import BME280 as BME280Sensor, LTR559 as LTR559Sensor

from instruments.enviro import Enviro
from instruments.hardware import Hardware


class Sensors:
    @staticmethod
    def poll(bme280_sensor: BME280Sensor, ltr559_sensor: LTR559Sensor) -> None:
        Enviro.poll(bme280_sensor, ltr559_sensor)
        Hardware.poll()
