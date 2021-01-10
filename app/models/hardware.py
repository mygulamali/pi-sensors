import subprocess
from typing import Dict, List, Optional

import psutil
from pydantic import BaseModel


CPU_TEMP_COMMAND: List[str] = ['cat', '/sys/class/thermal/thermal_zone0/temp']
CPU_PERCENT_INTERVAL: float = 0.1

class CPU(BaseModel):
    load_01: float
    load_05: float
    load_15: float
    percent: float
    temperature: Optional[float]

    @classmethod
    def poll(cls) -> 'CPU':
        load_avg = psutil.getloadavg()

        return CPU(
            load_01=load_avg[0],
            load_05=load_avg[1],
            load_15=load_avg[2],
            percent=psutil.cpu_percent(interval=CPU_PERCENT_INTERVAL),
            temperature=cls._cpu_temperature(),
        )

    @classmethod
    def _cpu_temperature(cls) -> Optional[float]:
        command = subprocess.Popen(CPU_TEMP_COMMAND, stdout=subprocess.PIPE)
        temperature = command.communicate()[0]

        if not temperature:
            return None

        return float(temperature) / 1000.0


class Memory(BaseModel):
    available_bytes: int
    total_bytes: int
    used_percent: float

    @classmethod
    def poll(cls) -> 'Memory':
        memory = psutil.virtual_memory()

        return Memory(
            available_bytes=memory.available,
            total_bytes=memory.total,
            used_percent=memory.percent,
        )


class Disk(BaseModel):
    device: str
    mountpoint: str
    free_bytes: int
    total_bytes: int
    used_percent: float

    @classmethod
    def poll(cls, device: str, mountpoint: str) -> 'Disk':
        disk_usage = psutil.disk_usage(mountpoint)

        return Disk(
            device=device,
            mountpoint=mountpoint,
            free_bytes=disk_usage.free,
            total_bytes=disk_usage.total,
            used_percent=disk_usage.percent,
        )


class Network(BaseModel):
    name: str
    address: Optional[str]
    received_bytes: int
    sent_bytes: int


class Hardware(BaseModel):
    cpu: CPU
    memory: Memory
    disks: List[Disk]
    networks: List[Network]

    @classmethod
    def poll(cls) -> 'Hardware':
        return Hardware(
            cpu=CPU.poll(),
            memory=Memory.poll(),
            disks=cls._disks(),
            networks=cls._networks()
        )

    @classmethod
    def _disks(cls) -> List[Disk]:
        return [
            Disk.poll(partition.device, partition.mountpoint)
            for partition in psutil.disk_partitions()
        ]

    @classmethod
    def _networks(cls) -> List[Network]:
        addresses = psutil.net_if_addrs()
        counters = psutil.net_io_counters(pernic=True)

        return [
            Network(
                name=nic,
                address=cls._network_address(nic, addresses),
                received_bytes=stats.bytes_recv,
                sent_bytes=stats.bytes_sent
            )
            for nic, stats in counters.items()
        ]

    @classmethod
    def _network_address(cls, nic: str, addresses: Dict) -> Optional[str]:
        if nic not in addresses:
            return None

        return addresses[nic][0].address
