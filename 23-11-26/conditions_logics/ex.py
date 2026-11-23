# %% ex1
age = int(input("Enter your age: "))
print("Adult" if age >= 18 else "Minor")

# %% ex2
number = int(input("Enter a number: "))
if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")


# %% ex3
number = int(input("Enter an integer number: "))
print("Even" if number % 2 == 0 else "Odd")


# %% ex4
num_1 = int(input("Enter first number: "))
num_2 = int(input("Enter second number: "))
if num_1 == num_2:
    print("Two numbers are equal")
else:
    print("max:", max(num_1, num_2))


# %% ex5
password = input("Enter a password: ")
if password == "Python123":
    print("Access Granted")
else:
    print("Access Denied")

# %% ex6
number = int(input("Enter a number: "))
if 1 <= number <= 10:
    print("belongs to 1-10 range")
elif 11 <= number <= 50:
    print("belongs to 11-50 range")
elif 51 <= number <= 100:
    print("belongs to 51-100 range")
else:
    print("out of defined ranges")


# %% ex7
grade = int(input("Enter grade: "))
if grade < 0 or grade > 100:
    print("Invalid Grade")
elif grade < 60:
    print("Failed")
elif grade < 70:
    print("Passed")
elif grade < 80:
    print("Good")
elif grade < 90:
    print("Very Good")
elif grade <= 100:
    print("Excellent")


# %% ex8
correct_username = "admin"
correct_password = "123456"
username = input("Enter username: ")
password = input("Enter password: ")
if username == correct_username and password == correct_username:
    print("Login Successful")
elif username == correct_username:
    print("Wrong Password")
else:
    print("Unknown User")


# %% ex9
age = int(input("Enter your age: "))
product_price = float(input("Enter product price: "))
discount_percent = 0
if age >= 60:
    discount_percent = 20
elif age < 18:
    discount_percent = 10
print("Total:", product_price - product_price * discount_percent / 100)

# %% ex10
number = int(input("Enter integer number: "))
if number % 3 == 0 and number % 5 == 0:
    print(f"{number} devided by 3 and by 5")
elif number % 3 == 0:
    print(f"{number} devided by 3")
elif number % 5 == 0:
    print(f"{number} devided by 5")
else:
    print(f"{number} is not devided by 3 or by 5")


# %% ex11
age = int(input("Enter your age: "))
has_companion = input("Do you have a companion? [y/n]: ").strip().lower()
while has_companion not in ['y', 'n']:
    has_companion = input("Do you have a companion? [y/n]: ").strip().lower()
has_companion = True if has_companion == 'y' else False
if age >= 18 or has_companion:
    print("Access Granted")
else:
    print("Access Denied")

# %% ex12
average_grade = float(input("Enter your average of grades: "))
monthly_salary = float(input("Enter your monthly salary: "))
if average_grade >= 90 or average_grade >= 85 and monthly_salary < 5000:
    print("You are eligible for a scholarship")
else:
    print("You are not eligible for a scholarship")


# %% ex13
correct_username = "admin"
correct_password = "123456"
username = input("Enter username: ")
password = input("Enter password: ")
is_active = input("Are you active? [y/n]: ").strip().lower()
while is_active not in ['y', 'n']:
    is_active = input("Are you active? [y/n]: ").strip().lower()
is_active = True if is_active == 'y' else False
if username == correct_username and \
    password == correct_username and \
    is_active:
        print("Access Granted")
else:
    print("Access Denied")


# %% ex14
number = int(input("Enter an integer number: "))
if 20 <= number <= 80:
    print(f"number {number} between 20 to 80!")
if not number < 20 and not number > 80:
    print(f"number {number} between 20 to 80!")


# %% ex15
balance = 5000
withdrawal = int(input("Enter amount for withdrawal"))
if withdrawal > 0:
    if withdrawal < balance:
        balance -= withdrawal
        print(f"withdrawal of {withdrawal} done successfully")
    else:
        print(f"not enough money. balance is: {balance}")
else:
    print("withdrawal must be a positive number")

# %% ex 16
age = int(input("Enter your age: "))
is_member = input("Are you a club member? [y/n]: ").strip().lower()
while is_member not in ['y', 'n']:
    is_member = input("Are you a club member? [y/n]: ").strip().lower()
is_member = True if is_member == 'y' else False
if age < 12:
    base_price = 25
elif age < 18:
    base_price = 35
else:
    base_price = 50
total = base_price - is_member * base_price * 10 / 100
print("Total price:", total)


# %% ex17
age = int(input("Enter your age: "))
monthly_salary = int(input("Enter your monthly salary: "))
seniority_in_months = int(input("Enter your seniority in months"))
if age < 21:
    print("Loan not approved. You must be over 21 years old")
elif monthly_salary < 7000:
    print("Loan not approved. Your salary must be over 7000")
elif seniority_in_months < 12:
    print("Loan not approved. Your seniority must be over a year")
else:
    print("Loan approved!")


# %% ex18
vehicle_type = input("Enter your vehicle type [motorcycle / private / commerical]").lower()
if vehicle_type not in ["motorcycle", "private", "commerical"]:
    vehicle_type = input("Enter your vehicle type [motorcycle / private / commerical]").lower()
parking_hours = float(input("Enter parking time in hours: "))

if vehicle_type == "motorcycle":
    hour_price = 10
elif vehicle_type == "private":
    hour_price = 20
else:
    hour_price = 30

price = hour_price * parking_hours
if parking_hours < 1:
    price -= price * 10 / 100
if parking_hours >= 5:
    price -= price * 15 / 100

print("Price:", price)

# %% ex19
num_1 = int(input("Enter first number: "))
num_2 = int(input("Enter second number: "))
operator = input("Enter operator [+, -, *, /]").strip().lower()
if operator not in ['+', '-', '*', '/']:
    print("Invalid operator")
    operator = input("Please enter a valid operator [+, -, *, /]").strip().lower()

match operator:
    case '+':
        print(f"{num_1} + {num_2} = {num_1 + num_2}")
    case '-':
        print(f"{num_1} - {num_2} = {num_1 - num_2}")
    case '*':
        print(f"{num_1} * {num_2} = {num_1 * num_2}")
    case '/':
        if num_2 == 0:
            print("Cannod divide by zero!")
        else:
            print(f"{num_1} / {num_2} = {num_1 / num_2}")

# %% ex20
year = int(input("Enter a year"))
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print("Leap year")
else:
    print("Regular year")


# %% ex21
base_price = 50
extra_125 = 0
extra_150 = 0

hours = int(input("Enter num of working hours: "))
if hours > 184:
    extra_150 = hours - 184
    hours = 184
if hours > 182:
    extra_125 = hours - 182
    hours = 182

total = base_price * hours + \
    extra_125 * base_price * 125 / 100 + \
    extra_150 * base_price * 150 / 100 

print("Total:", total)


# %% Project

age = int(input("Enter your age: "))
amount = float(input("Enter the purchase amount"))
passed_days = int(input("How many days ago did you purchase the product?"))
is_member = input("Are you a club member? [y/n]: ").strip().lower()
while is_member not in ['y', 'n']:
    is_member = input("Are you a club member? [y/n]: ").strip().lower()
is_member = True if is_member == 'y' else False
is_opened = input("Has the product been opened? [y/n]: ").strip().lower()
while is_opened not in ['y', 'n']:
    is_opened = input("Has the product been opened? [y/n]: ").strip().lower()
is_opened = True if is_opened == 'y' else False
has_invoice = input("Is there a purchase invoice? [y/n]: ").strip().lower()
while has_invoice not in ['y', 'n']:
    has_invoice = input("Is there a purchase invoice? [y/n]: ").strip().lower()
has_invoice = True if has_invoice == 'y' else False

if not has_invoice:
    print("Returns are possible only if an invoice is provided")
elif is_opened:
    print("Opened products cannot be returned")
elif amount <= 0:
    print("The purchase amount must be greater than zero")
elif not is_member and passed_days > 14:
    print("A regular customers may only receive a refund within 14 days")
elif is_member and passed_days > 30:
    print("Club members may receive a refund within 30 days")
else:
    print(f"Eligible for a refund of {amount}")


# %%
