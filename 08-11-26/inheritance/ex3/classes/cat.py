from .animal import Animal

class Cat(Animal):
    def climb(self):
        return f"{self.name} climbs the tree"
