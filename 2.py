numeric_input = int(input("Enter a number: "))


def sum_odd(num):
    total = 0
    for i in range(num + 1):
        if i % 2 == 0:
            continue
        else:
            total += i
    return total


print(sum_odd(numeric_input))
