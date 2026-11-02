def format_receipt(items):
    def line(name, price):
        return f"{name.ljust(10)}{price}"

    result = []
    for name, price in items:
        result.append(line(name, price))

    return "\n".join(result)

print(format_receipt([("Milk", 6), ("Bread", 9)]))
