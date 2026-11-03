# def show_total(prices):
#     total = 0
#     for price in prices:
#         total = total + price
#     print("Total:", total)


def calculate_total(prices):
    total = 0
    for price in prices:
        total = total + price
    return total

def show_total(prices):
    total = calculate_total(prices)
    print("Total:", total)

show_total([10, 20, 30])
