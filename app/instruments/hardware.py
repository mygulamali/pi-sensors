from instruments.cpu import CPU
from instruments.memory import Memory
from models import Hardware as Model


class Hardware:
    @staticmethod
    def poll() -> None:
        hardware = Model.poll()

        CPU(hardware.cpu)
        Memory(hardware.memory)
