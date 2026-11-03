# Wrong Code (the last line will show error. There is no variable named "message" in this scope):
# 
# def welcome(name):
#     message = "Welcome " + name
#     return message
 
# print(welcome("Dana"))
# print(message)

# Correct Code:
def welcome(name):
    message = "Welcome " + name
    return message

message = welcome("Dana")
print(message)
print(message)