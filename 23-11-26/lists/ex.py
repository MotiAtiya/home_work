# %% ex1
numbers = [10, 20, 30, 40, 50]
print(numbers)
print(numbers[0])
print(numbers[-1])
print(numbers[2])

# %% ex2
students = ['Rubi', 'Shimi', 'Levi', 'Yehuda']
print(len(students), "students")
print(students[0])
print(students[-1])
students[1] = 'Gad'
print(students)

# %% ex3
grades = [89, 91, 96, 93, 99]
grades.append(92)
grades.insert(0, 90)
grades[2] = 85
print(grades)

# %% ex4
numbers = [4, 6, 2, 9, 5, 1, 5, 6, 7, 3]
print(numbers)
del(numbers[0])
print(numbers)
numbers.pop()
print(numbers)
numbers.pop(3)
print(numbers)

# %% ex5
products = ['Milk', 'Eggs', 'Water', 'Bread', 'Solt']
print("Eggs is in the list?", 'Eggs' in products)
print("Ketchup is not in the list?", 'Ketchup' not in products)


# %% ex6
numbers = [45, 23, 87, 18, 42, 90, 58, 42, 13, 42]
for num in numbers:
    print(num)


# %% ex7
numbers = [45, 23, 87, 18, 42, 90, 58, 42, 13, 42]
for num in numbers:
    if num % 2 == 0:
        print(num)


# %% ex8
total = 0
grades = [89, 91, 96, 93, 99]
for grade in grades:
    total += grade
print("Total:", total)


# %% ex9
numbers = [45, 23, 87, 18, 42, 90, 58, 42, 13, 42]
max = numbers[0]
for num in numbers:
    if num > max:
        max = num
print("Max:", max)

# %% ex10
names = ["Emma", "Liam", "Olivia", "Noah", "Sophia"]
search_name = input("Enter a name to search: ")
if search_name.title() in names:
    print("Found")
else:
    print("Not Found")

# %% ex11
numbers = [45, 23, 87, 18, 42, 90, 58, 42, 13, 42]
search_num = int(input("Enter a num to search: "))
for i in range(len(numbers)):
    if numbers[i] == search_num:
        print(f"number {search_num} in index {i}")


# %% ex12
numbers = [45, 23, 87, 18, 42, 90, 58, 42, 13, 42]
counter = 0
for num in numbers:
    if num > 50:
        counter += 1
print(f"{counter} numbers greater then 50")

# %% ex13
numbers = [45, 23, 87, 18, 42, 90, 58, 42, 13, 42]
even_numbers = []
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
print(even_numbers)

# %% ex14
names = ["Emma", "Liam", "Olivia", "Noah", "Sophia"]
i = 0
while i < len(names):
    print(i, names[i])
    i += 1


# %% ex15
numbers = [45, 23, 87, 18, 42, 90, 58, 42, 13, 42]
print(numbers[:3])
print(numbers[-3:])
print(numbers[2:7])
print(numbers[::-1])


# %% ex16
names = ["Emma", "Liam", "Olivia", "Noah", "Sophia", "Jack", "Harry", "Jacob", "George", "James"]
for i in range(len(names)):
    if i % 2 == 0:
        print(names[i])
    
for i in range(len(names)):
    if i % 2 != 0:
        print(names[i])
    
print(names[::-2])

# %% ex17
numbers = [45, 23, 87, 18, 42, 90, 58, 42, 13, 13, 86, 93, 25, 11, 70, 59, 28, 84, 17, 34]
list_1 = numbers[:10]
list_2 = numbers[10:]
list_3 = numbers[5:15]
print(numbers)
print(list_1)
print(list_2)
print(list_3)

# %%ex18
numbers = [42, 90, 58, 42, 13, 13, 86, 93, 25, 11, 70, 59, 28, 34]
list_1 = numbers[:int(len(numbers) / 2)]
list_2 = numbers[int(len(numbers) / 2):]
print(numbers)
print(list_1)
print(list_2)


# %% ex19
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
double = [num * 2 for num in numbers]
squar = [num ** 2 for num in numbers]
even = [num for num in numbers if num % 2 == 0]
greater_then_5 = [num for num in numbers if num > 5]
print(numbers)
print(double)
print(squar)
print(even)
print(greater_then_5)

# %% ex20
grades = [55, 90, 67, 100, 45, 82, 73, 30]
greater_then_60 = [grade for grade in grades if grade >= 60]
lower_then_60 = [grade for grade in grades if grade < 60]
factor_5 = [grade + 5 for grade in grades]
print(grades)
print(greater_then_60)
print(lower_then_60)
print(factor_5)

# %% ex21
names = ["Moshe", "David", "Dana", "Noa", "Michael", "Avi"]
names_len_4 = [name for name in names if len(name) >= 4]
names_upper = [name.upper() for name in names]
startswith_D = [name for name in names if name.startswith('D')]
print(names)
print(names_len_4)
print(names_upper)
print(startswith_D)

# %% ex22
numbers = [12, 7, 25, 30, 9, 44, 18, 3]
new_list = [num for num in numbers if num % 3 == 0 and num > 10]
print(numbers)
print(new_list)

# %% ex23
numbers = []
for i in range(10):
    num = int(input("Enter a number: "))
    numbers.append(num)
print(numbers)

max = numbers[0]
for num in numbers:
    if num > max:
        max = num
print("Max:", max)

min = numbers[0]
for num in numbers:
    if num < min:
        min = num
print("Min:", min)

sum = 0
for num in numbers:
    sum += num
print("Average:", sum / len(numbers))

# %% ex24
users = ["Admin", "Moti", "Eli", "Avi", "Daniel"]
name_for_search = input("Enter a username to search: ")
if name_for_search.title() in users:
    users.remove(name_for_search)
else:
    print("Name not found")
print(users)

# %% ex25
numbers = [12, 7, 25, 30, 9, 44, 18, 3, 65, 23]
even_numbers = [num for num in numbers if num % 2 == 0]
odd_numbers = [num for num in numbers if num % 2 == 1]
greater_then_20 = [num for num in numbers if num > 20]
print(numbers)
print(even_numbers)
print(odd_numbers)
print(greater_then_20)

# %% ex26
numbers = [12, 7, 25, 30, 9, 44, 18, 3, 65, 23]
num_for_search = int(input("Enter a num to search: "))
counter = 0
for num in numbers:
    if num == num_for_search:
        counter += 1
if counter:
    print(f"{num_for_search} appers {counter} times in list")
else:
    print(num_for_search, "not found")


# %% ex27
num_list_1 = [1, 2, 3, 4, 5]
num_list_2 = [10, 20, 30, 40, 50]
combine = num_list_1 + num_list_2
print(combine)
print(combine[:5])
print(combine[-5:])
print(combine[::-1])

# %% ex28
numbers = [12, 7, 25, 30, 9, 44, 18, 3, 65, 23]
new_num = int(input("Enter a new number: "))
for num in numbers:
    if new_num == num:
        print(f"{new_num} already exists")
        break
else:
    numbers.append(new_num)

print(numbers)


# %% Project
grades = [85, 72, 90, 55, 100, 63, 48, 77]
while True:
    print("""
    ===== Grades Management =====

    1. Show all grades
    2. Add a grade
    3. Search for a grade
    4. Remove a grade
    5. Show passing grades
    6. Show failing grades
    7. Show highest and lowest grade
    8. Show average grade
    9. Show first 3 grades
    10. Show grades in reverse
    0. Exit
    """)
    choice = int(input("Choice: "))
    match choice:
        case 1:
            for grade in grades:
                print(grade, end=' ')
        case 2:
            new_grade = int(input("Enter a new grade: "))
            grades.append(new_grade)
        case 3:
            grade_for_search = int(input("Enter a grade to search: "))
            for i in range(len(grades)):
                if grades[i] == grade_for_search:
                    print(i)
        case 4:
            grade_for_remove = int(input("Enter a grade to remove: "))
            if grade_for_remove in grades:
                grades.remove(grade_for_remove)
            else:
                print("Grade not found")
        case 5:
            print([grade for grade in grades if grade >= 60])
        case 6:
            print([grade for grade in grades if grade < 60])
        case 7:
            highest = lowest = grades[0]
            for grade in grades:
                if grade > highest:
                    highest = grade
                elif grade < lowest:
                    lowest = grade
            print("Highest:", highest)
            print("Lowest:", lowest)
        case 8:
            if not grades:
                print("There are no grades")
                continue
            sum = 0
            for grade in grades:
                sum += grade
            print("Average:", sum / len(grades))
        case 9:
            print(grades[:3])
        case 10:
            print(grades[::-1])
        case 0:
            break

# %%
