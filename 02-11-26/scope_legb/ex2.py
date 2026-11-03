x = "global"
 
def first():
    x = "local in first"
    print("1:", x)
 
def second():
    print("2:", x)
 
first()
second()
print("3:", x)

# excepted prints:
# 1. local in first
# 2. global
# 3. global
