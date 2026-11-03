def outer():
    message = "outer"
 
    def show():
        print("show:", message)
 
    def change():
        nonlocal message
        message = "changed"
 
    show()
    change()
    show()
 
outer()

# the output should print:
# show: outer
# show: changed
