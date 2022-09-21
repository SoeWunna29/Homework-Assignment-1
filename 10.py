def sum_of_division(x):
    sum = 1
    for i in range(2, x):
        if x % i == 0:
            sum += i
    return sum


def is_amicable(a, b):
    if sum_of_division(a) == b and sum_of_division(b) == a:
        return True
    else:
        return False


def amc(n):
    i = n + 1
    while i < 10000:
        j = 0
        while j < 10000:
            if is_amicable(i, j):
                return i
            j += 1
        i += 1


amc(5)
