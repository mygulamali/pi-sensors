from pydantic import BaseModel
try:
    from ltr559 import LTR559 as Sensor
except ImportError:
    from mocks import LTR559 as Sensor


class LTR559(BaseModel):
    lux: float
    proximity: int

    @classmethod
    def poll(cls, sensor: Sensor) -> 'LTR559':
        sensor.update_sensor()
        return LTR559(lux=sensor._lux, proximity=sensor._ps0)
