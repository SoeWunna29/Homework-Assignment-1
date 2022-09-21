def foo(a, b, c, d):
    num_list = [a, b, c, d]
    sorted_list = sorted(num_list)
    x = sorted_list[0]
    y = sorted_list[1]
    return x ** 2 + y ** 2


print(foo(1, 2, 3, 4))
print(foo(-3, 1, 5, 6))
