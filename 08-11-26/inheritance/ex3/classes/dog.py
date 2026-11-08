from .animal import Animal

class Dog(Animal):
    def fetch(self):
        return f"{self.name} brings back the ball"
