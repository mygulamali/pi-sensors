from pydantic import BaseModel
try:
    from bme280 import BME280 as Sensor
except ImportError:
    from mocks import BME280 as Sensor


class BME280(BaseModel):
    humidity: float
    pressure: float
    temperature: float

    @classmethod
    def poll(cls, sensor: Sensor) -> 'BME280':
        sensor.update_sensor()

        return BME280(
            humidity=sensor.humidity,
            pressure=sensor.pressure,
            temperature=sensor.temperature,
        )
