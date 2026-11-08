def half(text):
    try:
        number = int(text)
    except ValueError:
        print("not a number:", text)
    else:
        print("half is", number / 2)
    finally:
        print("checked", text)

half("8")
half("x")


# Expected Output for: half("8"):

# half if 4
# checked 8


# Expected Output for: half("x"):

# not a number: x
# checked x
