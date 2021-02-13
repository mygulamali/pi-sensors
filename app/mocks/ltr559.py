from mocks.base import Base


class LTR559(Base):
    @property
    def _lux(self) -> float:  # Lux
        return 100000.0 * self.value

    @property
    def _ps0(self) -> int:
        return int(1000.0 * self.value)
