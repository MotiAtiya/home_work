from classes.product import Product

pen = Product("Pen", 5)
print(pen.name, pen.price, pen.quantity)
try:
    Product("Bad", -10)
except ValueError as error:
    print("error:", error)
