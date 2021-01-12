from instruments.cpu import CPU
from instruments.memory import Memory


class Hardware:
    @staticmethod
    def poll() -> None:
        CPU.poll()
        Memory.poll()
