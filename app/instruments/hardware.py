from instruments.cpu import CPU
from instruments.disk import Disk
from instruments.memory import Memory
from instruments.network import Network
from models import Hardware as Model


class Hardware:
    @staticmethod
    def poll() -> None:
        hardware = Model.poll()

        CPU(hardware.cpu)
        for disk in hardware.disks:
            Disk(disk)
        Memory(hardware.memory)
        for network in hardware.networks:
            Network(network)
