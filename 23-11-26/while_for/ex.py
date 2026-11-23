# %% ex1
i = 1
while i <= 10:
    print(i)
    i += 1

# %% ex2
i = 10
while i >= 1:
    print(i)
    i -= 1
print("START!")

# %% ex3
i = 1
while i <= 50:
    if i % 2 == 0:
        print(i)
    i += 1

# %% ex4
num = int(input("Enter a number: "))
for i in range(1, 6):
    print(i * num)


# %% ex5
total = 0
for i in range(1, 101):
    total += i
print(total)

# %% ex6
correct_password = "Python123"
password = input("Enter a password: ")
while password != correct_password:
    print("Wrong password!")
    password = input("Enter a password: ")
print("Welcome!")


# %% ex7
secret_number = 27
number = int(input("Guess the number: "))
while number != secret_number:
    print("Wrong guess!")
    number = int(input("Guess the number: "))
print("Correct number!")


# %% ex8
total = 0
num = int(input("Enter an integer number to sum (0 to end): "))
while num != 0:
    total += num
    num = int(input("Enter an integer number to sum (0 to end): "))
print("Total:", total)

# %% ex9
total = 0
counter = 0
grade = int(input("Enter a grade (999 to end): "))
while grade != 999:
    counter += 1
    total += grade
    grade = int(input("Enter a grade (999 to end): "))
print(f"{counter} grades")
print(f"{total} in total")
if counter > 0:
    print(f"{total / counter} in average")


# %% ex10
total_positive = 0
counter = 0
num = int(input("Enter a number (enter negative to end): "))
while num >= 0:
    total_positive += num
    counter += 1
    num = int(input("Enter a number (enter negative to end): "))

print(f"{total_positive} in total")
print(f"{counter} numbers")


# %% ex11
number = int(input("Enter a number: "))
i = 1
while i <= 10:
    print(f"{number} x {i} = {number * i}")
    i += 1

# %% ex12
number = int(input("Enter an integer positive number: "))
counter = 0
while number:
    counter += 1
    number //= 10
print(counter, "digits")

# %% ex13
number = int(input("Enter an integer positive number: "))
while number:
    print(number % 10, end='')
    number //= 10

# %% ex14

number = int(input("Enter an integer positive number: "))
is_prime = True
if number < 2:
    is_prime = False
i = 2
while i * i <= number:
    if number % i == 0:
        is_prime = False
        break
    i += 1
if is_prime:
    print("is a prime number")
else:
    print("is not a prime number")
    

# %% ex15
balance = 5000
while True:
    print("""
====== ATM SYSTEM ======

1. Check balance
2. Deposit
3. Withdrawal
4. Exit

    """)
    choice = int(input("Enter your choice: "))
    match choice:
        case 1:
            print("Balance:", balance)
        case 2:
            deposit = int(input("Enter the amount to deposit"))
            if deposit <= 0:
                print("Must be positive number")
            # elif amount > balance:
            #     print("Not enough money")
            else:
                balance += deposit
        case 3:
            withdraw = int(input("Enter the amount to withdraw"))
            if withdraw <= 0:
                print("Must be positive number")
            elif withdraw > balance:
                print("Not enough money")
            else:
                balance -= withdraw
        case 4:
            print("Bye!")
            break
        case _:
            print("Invalid choice")
            
# %% ex16
i = 1
while True:
    print(i)
    if i == 15:
        break
    i += 1

# %% ex17
i = 0
while i < 30:
    i += 1
    if i % 3 == 0:
        continue
    print(i)
    
# %% ex18
while True:
    num = int(input("Enter a number: (100 to stop)"))
    if num == 100:
        print("User stopped")
        break

# %% ex19
for i in range(1, 21):
    print(i)


# %% ex20
for i in range(0, 101, 5):
    print(i)


# %% ex21
total = 0
for i in range(1, 101):
    total += i
print("Total:", total)

# %% ex22
number = int(input("Enter a number: "))
for i in range(1, 11):
    print(number * i)

# %% ex23
start = int(input("Enter start number"))
end = int(input("Enter end number"))
result = 0
for i in range(start, end+1):
    result += i
print("Result:", result)

# %% ex24
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print(i)
# %% ex25
rows = int(input("Enter num of rows: "))
cols = int(input("Enter num of columns: "))
for i in range(rows):
    for j in range(cols):
        print('*', end='')
    print()
# %% ex26
for i in range(1, 7):
    for j in range(i):
        print('*', end='')
    print()

# %% ex27
for i in range(1, 11):
    for j in range(1, 11):
        print(i * j, end='\t')
    print()


# %% ex28
for i in range(1, 6):
    for j in range(i, 6):
        print(i, j)

# %% Project
result = 0
while True:
    print("""
# ===== MATH GAME =====

# 1. Start Game
# 2. View Instructions
# 3. Exit
    """)
    choice = int(input("Choose: "))
    match choice:
        case 1:
            for i in range(1, 11):
                num_1 = (i * 5 + 7) // 3
                num_2 = (i * 8 - 7) // 3
                answer = int(input(f"{num_1} + {num_2}"))
                if answer == num_1 + num_2:
                    print("Correct!")
                    result += 1
                else:
                    print("Wrong")
        case 2:
            print("Math Game with 10 question. Every correct answer add you a point!")
        case 3:
            print("Bye")
            break


# %%
