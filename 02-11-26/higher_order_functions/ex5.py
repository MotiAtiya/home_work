def apply_to_all(numbers, action):
    result = []
    for num in numbers:
        result.append(action(num))
    return result


def double(n):
    return n * 2

# the folowing code wil not work, becouse it call the function, not pass it as a referance:
# print(apply_to_all([1, 2], double()))

# this is the correct code:
print(apply_to_all([1, 2], double))