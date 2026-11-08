student1 = {"name": "Dana", "grades": [90, 85]}
student2 = {"name": "Avi", "grades": [70]}
student3 = {"nmae": "Noa", "grades": []}
 
def average(student):
    return sum(student["grades"]) / len(student["grades"])


print(average(student3))

# The problems:
# 1: line 3: typo nmae instead of name
# 2. line 6: if grades is empty, it will divide by zero
# 3. 