from mocks.base import Base


class BME280(Base):
    @property
    def humidity(self) -> float:
        return self.value

    @property
    def pressure(self) -> float:
        return 101325.0 * self.value

    @property
    def temperature(self) -> float:
        return 100.0 * self.value
