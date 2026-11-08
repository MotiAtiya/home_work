from classes.product import Product

laptop = Product("Laptop", 1000)
mouse = Product("Mouse", 50)
print(Product.created_count)
print(laptop.price_with_vat())
