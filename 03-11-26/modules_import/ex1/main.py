import price

if __name__ == "__main__":
    price_after_discount = price.apply_discount(200, 10)
    print("After discount", price_after_discount)
    price_after_discount_with_vat = price.add_vat(price_after_discount)
    print("With VAT", price_after_discount_with_vat)
