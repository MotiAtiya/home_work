def add(price, cart):
    cart.append(price)

cart = []
add(100, cart)
add(50, cart)
total = sum(cart)
print(cart, total)
