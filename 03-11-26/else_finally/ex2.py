def check(number):
    try:
        if number > 0:
            return "positive"
        return "not positive"
    finally:
        print("done checking", number)

print(check(5))
print(check(-2))


# Expected Output for: print(check(5)):

# done checking 5
# positive


# Expected Output for: print(check(-2)):

# done checking -2
# not positive

# finally runs first before return