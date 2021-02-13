from pydantic import BaseModel
try:
    from bme280 import BME280
    from ltr559 import LTR559
except ImportError:
    from mocks import BME280, LTR559

from models.enviro import Enviro
from models.hardware import Hardware


class Sensors(BaseModel):
    enviro: Enviro
    hardware: Hardware

    @classmethod
    def poll(cls, bme280: BME280, ltr559: LTR559) -> 'Sensors':
        return Sensors(
            enviro=Enviro.poll(bme280, ltr559),
            hardware=Hardware.poll(),
        )
