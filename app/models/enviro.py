from pydantic import BaseModel

try:
    from bme280 import BME280 as BME280Sensor
    from ltr559 import LTR559 as LTR559Sensor
except ImportError:
    from mocks import BME280 as BME280Sensor, LTR559 as LTR559Sensor

from models.bme280 import BME280
from models.ltr559 import LTR559


class Enviro(BaseModel):
    bme280: BME280
    ltr559: LTR559

    @classmethod
    def poll(cls, bme280_sensor: BME280Sensor, ltr559_sensor: LTR559Sensor) -> "Enviro":
        return Enviro(
            bme280=BME280.poll(bme280_sensor),
            ltr559=LTR559.poll(ltr559_sensor),
        )
