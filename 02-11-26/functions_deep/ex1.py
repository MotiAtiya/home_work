def make_greeting(name, greeting="Hello", punct="!"):
    return f"{greeting}, {name}{punct}"


print(make_greeting("Dana"))
print(make_greeting("Avi", "Good morning"))
print(make_greeting("Noa", punct="?"))
