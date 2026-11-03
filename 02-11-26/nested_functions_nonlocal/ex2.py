def make_greeter(greeting):
    def message(name):
        return f"{greeting}, {name}"
    return message

hello = make_greeter("Hello")
shalom = make_greeter("Shalom")
print(hello("Dana"))
print(shalom("Avi"))
