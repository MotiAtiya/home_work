from .customer import Customer

class Order:
    def __init__(self, customer:Customer, price):
        self.customer = customer
        self.price = price
    