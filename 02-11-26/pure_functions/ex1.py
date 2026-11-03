# pure:
def square(n):
    return n * n

#  pure
def log_square(n):
    print("squaring", n)
    return n * n

#  not pure, side effect: change the original cert list
def add_item(cart, item):
    cart.append(item)
    return cart

# not pure, side effect: change the original cert list
def with_item(cart, item):
    return cart + [item]
