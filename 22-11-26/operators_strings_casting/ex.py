# %% ex1
num1 = 25
num2 = 7

print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} * {num2} = {num1 * num2}")
print(f"{num1} / {num2} = {num1 / num2}")
print(f"{num1} // {num2} = {num1 // num2}")
print(f"{num1} % {num2} = {num1 % num2}")
print(f"{num1} ** {num2} = {num1 ** num2}")

# %% ex2
balance = 1000
print(balance)
balance += 250
print(balance)
balance -= 100
print(balance)
balance *= 2
print(balance)
balance /= 4
print(balance)


# %% ex3
product_price = float(input("Enter product price"))
percent_discount = float(input("Enter product price"))
discount = product_price * percent_discount / 100
print("Discount:", discount)
print("Last price (after discount):", product_price - discount)

# %% ex4
amount = float(input("Enter amount: "))
interest_rate = float(input("Enter interest rate: "))
print("One year interest rate:", interest_rate * amount / 100)
print("Amount with interest rate:", amount + interest_rate * amount / 100)
# %% ex5
grade_1 = float(input("Enter first grade: "))
grade_2 = float(input("Enter second grade: "))
grade_3 = float(input("Enter third grade: "))
print("Average:", (grade_1 + grade_2 + grade_3) / 3)

# %% ex6
first_name = "David"
last_name = "Cohen"
city = "Tel Aviv"
# print("Hello, my name is " + first_name + " " + last_name + " and I live in " + city + ".")
print(f"Hello, my name is {first_name} {last_name} and I live in {city}.")
# %% ex7
full_name = input("Enter your full name: ")
print("Full name:", full_name)
print("Full name len:", len(full_name))
print(full_name.lower())
print(full_name.upper())
# %% ex8
sentence = input("Enter a sentence: ")
print(sentence.upper())
print(sentence.lower())
print(sentence.capitalize())
print(sentence.title())
# %% ex9
full_name = input("Enter your full name: ")
print("original:", full_name)
print("clean:", full_name.strip())
print("len original:", len(full_name))
print("len clean:", len(full_name.strip()))

# %% ex10
sentence = "I love Java programming"
print(sentence.replace("Java", "Python"))
print("num of 'love':", sentence.count("love"))
print("Starts with 'I':", sentence.startswith("I"))
print("Ends with 'programming':", sentence.endswith("programming"))
# %% ex11
word = "Programming"
print("First char:", word[0])
print("Last char:", word[-1])
print("Third char:", word[2])
print("First three chars:", word[:3])
print("Last four chars:", word[-4:])
print("Reverse word:", word[::-1])

# %% ex12
a = "100"
b = "25"
c = 10
d = 5.5

a = int(a)
b = float(b)
c = str(c)
d = int(d)

print("a", a, type(a))
print("b", b, type(b))
print("c", c, type(c))
print("d", d, type(d))

# %% ex13
age = input("Enter your age: ")

# print(age + 10) # Operator "+" not supported for types "str" and "int"
print(int(age) + 10)

# %% ex14
product_price = float(input("Enter product price (without tax): "))
price_with_tax = product_price + product_price * 18 / 100
print("last price:", price_with_tax)

# %% ex15
first_name = input("First name: ")
last_name = input("Last name: ")
age = float(input("Age: "))
monthly_salary = float(input("Monthly salary: "))
seniority_years = int(input("Number of years of seniority: "))

print(f"""======== Worker Details ========
{first_name.title()} {last_name.title()}, {age}
Monthly Salary: {monthly_salary}
Seniority Years: {seniority_years}
Yearly Salary: {monthly_salary * 12}
Monthly Salary With Bonus: {monthly_salary + monthly_salary * 5 / 100}
Full Name Length: {len(first_name.strip()) + len(last_name.strip())}
""")



# %% ex16
amount = float(input("Enter amount: "))
usd_rate = 3.25
euro_rate = 3.75
conversion_fee = 2
print("Amount (Dollar):", amount * usd_rate)
print("Amount (Euro):", amount * euro_rate)
print("Amount with conversion fee:", amount + amount * conversion_fee / 100)


# %% ex17
first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
year_of_birth = int(input("Enter year of birth: "))
email = f"{first_name}.{last_name}.{year_of_birth}@gmail.com".lower()
print("Email:", email)

# %% ex18
# כתבו תוכנית שמבקשת מהמשתמש להכניס משפט.
# הציגו את הנתונים הבאים:
# המשפט המקורי.
# מספר התווים במשפט.
# המשפט באותיות גדולות.
# המשפט באותיות קטנות.
# המשפט בסדר הפוך.
# מספר הפעמים שהאות a מופיעה במשפט.
# המשפט לאחר החלפת רווחים במקפים באמצעות replace().

sentence = input("Enter a sentence: ").strip()
print("Original sentence:", sentence)
print("Sentence length:", len(sentence))
print(sentence.upper())
print(sentence.lower())
print(sentence[::-1])
print("num of 'a':", sentence.count('a'))
print(sentence.replace(' ', '-'))

# %% Project

customer_name = input("Enter customer name: ")
product_name = input("Enter product name: ")
product_price = float(input("Enter product price: "))
quantity = int(input("Enter quantity: "))
discount_percent = float(input("Enter discount percent"))
vat_percent = float(input("Enter vat percent"))

subtotal = quantity * product_price
discount = subtotal * discount_percent / 100
after_discount = subtotal - discount
vat_amount = after_discount * vat_percent / 100

print(f"""
================================
          PURCHASE INVOICE
================================

Customer: {customer_name}
Product: {product_name}

Unit Price: {product_price}
Quantity: {quantity}

Subtotal: {subtotal}
Discount: {discount}
After Discount: {after_discount}

VAT: {vat_percent}%
VAT Amount: {vat_amount}

TOTAL: {after_discount + vat_amount}

================================
       THANK YOU FOR SHOPPING
================================
""")


# %%
