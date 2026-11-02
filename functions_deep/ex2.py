def average(*numbers):
    if not numbers:
        raise ValueError("need at least one number")
    return sum(numbers) / len(numbers)

print(average(80, 90))
print(average(70, 80, 90, 100))
try:
    average()
except ValueError as error:
    print("error:", error)
