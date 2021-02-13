from mocks.base import Base


class LTR559(Base):
    @property
    def _lux(self):
        return 100000.0 * self.value

    @property
    def _ps0(self):
        return int(1000.0 * self.value)
