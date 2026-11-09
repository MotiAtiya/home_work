from .cpu import CPU
from .ram import RAM
from .disk import Disk

class Computer:
    def __init__(self, cpu:CPU, ram:RAM, disk:Disk):
        self.cpu, self.ram, self.disk = cpu, ram, disk

    def __str__(self) -> str:
        return f"{self.cpu.cores}-core {self.cpu.speed}GHz CPU, {self.ram.gb_size}GB RAM, {self.disk.gb_size}GB SSD"

    def can_run(self, min_cores, min_speed):
        return min_cores >= self.cpu.cores and min_speed >= self.ram.gb_size

