# Wrong Code:
# left count is a local variable, so right count cannot be the global variable

# count = 0
 
# def add_one():
#     count = count + 1
 
# add_one()


# 3 correct options to fix (the last one is recommended):

# Correct Code - Option 1:
# count = 0
 
# def add_one():
#     c = count + 1
 
# add_one()

# Correct Code - Option 2:
# count = 0
 
# def add_one():
#     global count
#     count = count + 1
 
# add_one()

# Correct Code - Option 3:
# count = 0
 
# def add_one(count):
#     count = count + 1
 
# add_one(count)
