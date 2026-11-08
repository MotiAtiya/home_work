from classes.user import User

user = User(30)
user.age = user.age + 1
print(user.age)
try:
    user.age = -5
except ValueError as error:
    print("error:", error)
print(user.age)
