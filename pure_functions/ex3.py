TAX = 1.17
 
def apply_tax(prices):
    result = []
    for i in range(len(prices)):
        result.append(round((prices[i] * TAX), 2))
    return result


prices = [100, 50]
with_tax = apply_tax(prices)
print(prices)
print(with_tax)
