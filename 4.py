def df(a, b, c):
    if a - b == c or c - b == a or b - c == a or a - c == b:
        print("True")
    else:
        print("False")


df(5, 3, 2)
df(2, 3, 5)
df(2, 5, 3)
df(-2, 3, 5)
df(2, 3, -5)
df(10, 6, 3)
