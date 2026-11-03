def make_discount(percent):
    def discount(n):
        return n - n * percent / 100
    return discount

ten_off = make_discount(10)
half_price = make_discount(50)
print(ten_off(200))
print(half_price(200))
