products = [("Laptop", 3500), ("Mouse", 80), ("Desk", 900)]

sorted_product = sorted(products, key=lambda p: p[1])
for p in sorted_product:
    print(p[0], p[1])

print("Most expensive:", sorted_product[-1][0])
