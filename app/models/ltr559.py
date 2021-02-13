from ltr559 import LTR559 as Sensor
from pydantic import BaseModel


class LTR559(BaseModel):
    lux: float
    proximity: int

    @classmethod
    def poll(cls, sensor: Sensor) -> 'LTR559':
        sensor.update_sensor()
        return LTR559(lux=sensor._lux, proximity=sensor._ps0)
