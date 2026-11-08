class Product:
    VAT_RATE = 0.17
    created_count = 0

    def __init__(self, name, price):
        self.name = name
        self.price = price
        Product.created_count += 1

    def price_with_vat(self):
        return self.price + self.price * Product.VAT_RATE


    def get_count(self):
        return self.created_count