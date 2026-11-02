def make_counter(step):
    counter = 0

    def increase():
        nonlocal counter
        counter += step
        return counter
    
    return increase


by_two = make_counter(2)
by_ten = make_counter(10)
print(by_two(), by_two())
print(by_ten())
print(by_two())
