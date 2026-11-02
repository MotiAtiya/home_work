# 1. in this code, the second call will print: '["milk", "bread"].
# but this is not correct, because the function want to initialize the cart
# if you didn't padd a cart to parameter.

# def add_item(item, cart=[]):
#     cart.append(item)
#     return cart
 
# print(add_item("milk"))
# print(add_item("bread"))


# Correct Code:
def add_item(item, cart=None):
    if not cart:
        cart = []
    cart.append(item)
    return cart
 
print(add_item("milk"))
print(add_item("bread"))
