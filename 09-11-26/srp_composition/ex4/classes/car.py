from .engine import Engine

class Car:
    def __init__(self, model, engine:Engine):
        self.model, self.engine = model, engine

    def start(self):
        return f"{self.model}: engine {self.engine.horsepower}hp started"
