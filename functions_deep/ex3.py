def format_profile(name, **details):
    detail_list = []
    for d in details:
        detail_list.append(f"{d}={d[1]}")
    return f"{name}: {' '.join(detail_list)}"


print(format_profile("Dana", age=24, city="Haifa"))
print(format_profile("Avi"))
