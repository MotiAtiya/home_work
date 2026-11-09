from classes import *

pc = Computer(CPU(8, 3.2), RAM(8), Disk(512))
print(pc)
print("Can run the game?", pc.can_run(6, 16))
