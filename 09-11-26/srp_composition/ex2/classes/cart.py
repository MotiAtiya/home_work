from .product import Product

class Cart:
    def __init__(self):
        self.products = []

    def add(self, name, price, quantity=1):
        self.products.append(Product(name, price, quantity))

    def subtotal(self):
        return sum(p.price * p.quantity for p in self.products)
