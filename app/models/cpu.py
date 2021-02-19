import subprocess
from typing import List, Optional

import psutil
from pydantic import BaseModel


CPU_TEMP_COMMAND: List[str] = ["cat", "/sys/class/thermal/thermal_zone0/temp"]
CPU_PERCENT_INTERVAL: float = 0.1


class CPU(BaseModel):
    load_01: float
    load_05: float
    load_15: float
    percent: float
    temperature: Optional[float]

    @classmethod
    def poll(cls) -> "CPU":
        load_avg = psutil.getloadavg()

        return CPU(
            load_01=load_avg[0],
            load_05=load_avg[1],
            load_15=load_avg[2],
            percent=psutil.cpu_percent(interval=CPU_PERCENT_INTERVAL),
            temperature=cls._cpu_temperature(),
        )

    @staticmethod
    def _cpu_temperature() -> Optional[float]:
        command = subprocess.Popen(CPU_TEMP_COMMAND, stdout=subprocess.PIPE)
        temperature = command.communicate()[0]

        if not temperature:
            return None

        return float(temperature) / 1000.0
