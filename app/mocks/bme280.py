from mocks.base import Base


class BME280(Base):
    @property
    def humidity(self) -> float:  # %
        return 100.0 * self.value

    @property
    def pressure(self) -> float:  # hPa
        return 1013.25 * self.value

    @property
    def temperature(self) -> float:  # ºC
        return 100.0 * self.value
