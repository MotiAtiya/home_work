# Wrong Code:
# the list variable override the build-in list function. so you cannot call it later
# this happen because local variables are called before built-in variables or functinos,
# according to the LEGB priorities

# list = [1, 2, 3]
# numbers = list(range(5))

# Correct Code:
my_list = [1, 2, 3]
numbers = list(range(5))
