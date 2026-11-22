
# ex1
# first_name = "Moti"
# last_name = "Atiya"
# age = 30
# city = "Jerusalem"
# email = "a.moti96@gmail.com"

# print("===== User Details =====")
# print("First Name:", first_name)
# print("Last Name:", last_name)
# print("Age:", age)
# print("City:", city)
# print("Email:", email)
# print("========================")


# ex2
# birth_year = 1996
# current_year = 2026
# age = current_year - birth_year
# print(f"You are approximately {age} years old.")


# ex3
# width = 10
# height = 20
# area = width * height
# perimeter = width * 2 + height * 2
# print("Area:", area)
# print("Perimeter:", perimeter)


# ex4
# name = "David"
# age = 25
# height = 1.78
# is_student = True
# salary = 8500

# print("Name:", name, type(name))
# print("Age:", age, type(age))
# print("Height:", height, type(height))
# print("Is Student:", is_student, type(is_student))
# print("Salary:", salary, type(salary))



# ex5
# first_name = input("Enter your first name: ")
# last_name = input("Enter your last name: ")
# city = input("Enter your city: ")
# age = int(input("Enter your age: "))

# print(f"Welcome {first_name} {last_name}!")
# print(f"Your are {age} years old, and live in {city}.")



# ex6
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# print(f"{a} + {b} = {a+b}")
# print(f"{a} - {b} = {a-b}")
# print(f"{a} * {b} = {a*b}")
# print(f"{a} / {b} = {a/b}")


# ex7
# product_name = input("Enter product name: ")
# product_price = int(input("Enter product price: "))
# quantity = int(input("Enter quantity: "))

# print("====== Purchase Receipt ======")
# print("Product:", product_name)
# print("Price:", product_price)
# print("Quantity:", quantity)
# print("Total", quantity * product_price)
# print("==============================")



# ex9
# name = input("Name: ")
# hours = float(input("Hours: "))
# rate = float(input("Rate: "))

# print("====== Monthly Report ======")
# print("Name: ", name)
# print("Salary: ", hours * rate)


# ex10
# total = float(input("Total account: "))
# tip_percentage = float(input("Tip percentage: "))
# num_of_diners = int(input("Number of diners: "))

# tip = total * tip_percentage / 100
# total_payment = total + tip

# print("Tip:", tip)
# print("Total payment including tip:", total_payment)
# print("Payment for diner:", (total_payment) / num_of_diners)


# ex11
# a = 10
# b = 20
# print("a", a)
# print("b", b)
# temp = a
# a = b
# b = temp
# print("a", a)
# print("b", b)


# Project

print("====== Students Registration System ======")
first_name = input("First Name: ")
last_name = input("Last Name: ")
age = float(input("Age: "))
institution = input("Institution Name: ")
course_name = input("Course Name: ")
duration = float(input("Duration (in months): "))
monthly_price = int(input("Monthly Price: "))


print(f"""
================================
       STUDENT REGISTRATION
================================

Student: {first_name} {last_name}
Age: {age}
Institution: {institution}
Course: {course_name}
Duration: {duration}
Monthly Price: {monthly_price}

Total Course Price: {duration * monthly_price}

================================
Registration completed!
================================
""")
