def unique_digits(x):
    number = str(x)
    unique = sorted([int(x) for x in set(number)])

    print(f"Unique digits in {number} are {unique}")
    print("Total unique digits are " + str(len(unique)))


unique_digits(15464658)
