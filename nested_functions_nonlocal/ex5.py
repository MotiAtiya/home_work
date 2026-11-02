# def make_counter():
#     count = 0
#     def increment():
#         count += 1
#         return count
#     return increment
 
# counter = make_counter()
# counter()


# 1. the error is: UnboundLocalError
#    the count in increment function cannot access to the count in make_counter functino
# 2. nonlocal is for variables in outer function (the functino that wraps our function)
#    global is for global variables, in the root of the python file
