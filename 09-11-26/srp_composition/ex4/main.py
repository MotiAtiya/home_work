# Wrong code:
# class Engine:
#     def start(self):
#         return "engine started"
 
# class Car(Engine):
#     def __init__(self, model):
#         self.model = model

# Car is not an Engine. but car has an engine


from classes import *

car = Car("Mazda", Engine(150))
print(car.start())
