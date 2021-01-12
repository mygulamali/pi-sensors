from typing import Dict, List, Optional

import psutil
from pydantic import BaseModel

from models.cpu import CPU
from models.disk import Disk
from models.memory import Memory
from models.network import Network


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

    @staticmethod
    def _disks() -> List[Disk]:
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
