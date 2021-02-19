try:
    from bme280 import BME280 as BME280Sensor
    from ltr559 import LTR559 as LTR559Sensor
except ImportError:
    from mocks import BME280 as BME280Sensor, LTR559 as LTR559Sensor

from instruments.bme280 import BME280
from instruments.ltr559 import LTR559
from models import Enviro as Model


class Enviro:
    @staticmethod
    def poll(
            bme280_sensor: BME280Sensor,
            ltr559_sensor: LTR559Sensor
    ) -> None:
        enviro = Model.poll(bme280_sensor, ltr559_sensor)

        BME280(enviro.bme280)
        LTR559(enviro.ltr559)
