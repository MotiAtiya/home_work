from classes import *

cart = Cart()
cart.add("Pen", 5, 4)
cart.add("Bag", 60)
checkout = Checkout(cart, IsraeliVat())
print(checkout.total())
