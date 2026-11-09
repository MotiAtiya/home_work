from classes import *

cart = Cart()
cart.add("Pen", 5, 4)
cart.add("Bag", 60)
checkout_1 = Checkout(cart, IsraeliVat())
checkout_2 = Checkout(cart, TaxExempt())
print(checkout_1.total())
print(checkout_2.total())
