from classes.animal import Animal
from classes.dog import Dog
from classes.cat import Cat

rex = Dog("Rex", 4)
mitzi = Cat("Mitzi", 5)
print(rex.describe(), "|", rex.fetch())
print(mitzi.describe(), "|", mitzi.climb())
