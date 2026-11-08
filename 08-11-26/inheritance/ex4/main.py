from classes.vehicle import Vehicle
from classes.truck import Truck

truck = Truck("Volvo", 1000)
truck.load(600)
print(truck.brand, truck.wheels, truck.load_kg)
try:
    truck.load(500)
except ValueError as error:
    print("error:", error)
