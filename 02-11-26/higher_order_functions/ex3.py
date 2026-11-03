words = ["banana", "fig", "cherry", "kiwi"]
students = [("Dana", 92), ("Avi", 78), ("Noa", 85)]

print(sorted(words, key=len))
print(max(words, key=len))

sorted_students_by_score = sorted(students, reverse=True, key=lambda s: s[1])
for s in sorted_students_by_score:
    print(s[0])
