from random import random


class Base:
    def __init__(self):
        self.value = -1.0

    def update_sensor(self) -> None:
        self.value = random()
