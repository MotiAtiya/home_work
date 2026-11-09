from .cart import Cart
from .israeli_vat import IsraeliVat

class Checkout:
    def __init__(self, cart:Cart, vat_calculator):
        self.cart, self.vat_calculator = cart, vat_calculator

    def total(self):
        return self.vat_calculator.apply(self.cart.subtotal())
