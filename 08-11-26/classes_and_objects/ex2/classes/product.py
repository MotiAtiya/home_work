class Product:
    def __init__(self, name, price, quantity=0):
        if price < 0:
            raise ValueError("Wrong input: Price cannot be negative")
        self.price = price
        self.name = name
        self.quantity = quantity
