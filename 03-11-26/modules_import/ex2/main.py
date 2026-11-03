# 3 Options to Import:

# 1
import price

if __name__ == "__main__":
    price_after_discount = price.apply_discount(200, 10)
    print("After discount", price_after_discount)
    price_after_discount_with_vat = price.add_vat(price_after_discount)
    print("With VAT", price_after_discount_with_vat)

# 2
from price import apply_discount, add_vat

if __name__ == "__main__":
    price_after_discount = apply_discount(200, 10)
    print("After discount", price_after_discount)
    price_after_discount_with_vat = add_vat(price_after_discount)
    print("With VAT", price_after_discount_with_vat)

# 3
import price as p

if __name__ == "__main__":
    price_after_discount = p.apply_discount(200, 10)
    print("After discount", price_after_discount)
    price_after_discount_with_vat = p.add_vat(price_after_discount)
    print("With VAT", price_after_discount_with_vat)
