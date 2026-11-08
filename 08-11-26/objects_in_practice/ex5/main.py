from classes.course import Course

course = Course("PY101", "Intro to Python", 2)
for student in ["Dana", "Avi", "Noa"]:
    print(student, course.enroll(student))
print(course)
try:
    course.enroll("Dana")
except ValueError as error:
    print("error:", error)
