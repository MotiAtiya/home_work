def top_three(numbers):
    sorted_desc = sorted(numbers, reverse=True)
    return sorted_desc[:3]


scores = [70, 95, 88, 60, 99]
print(top_three(scores))
print(scores)
