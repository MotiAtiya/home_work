def apply_to_all(numbers, action):
    result = []
    for num in numbers:
        result.append(action(num))
    return result

def double(num):
    return num * 2

# def round(num):
#     if num % 1 >= 0.5:
#         return int(num) + 1
#     return int(num)

print(apply_to_all([1, 2, 3], double))
print(apply_to_all([1, 2, 3], lambda n: n * n))
print(apply_to_all([1.6, 2.4], round))

