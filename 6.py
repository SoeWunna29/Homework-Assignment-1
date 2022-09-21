def perfect_integer(m):
    factorials = []
    for i in range(1, m):
        if m % i == 0:
            factorials.append(i)
    print(f"List of Factorials for {m} are {factorials}")
    sum = 0
    for j in factorials:
        sum += j
    if sum == m:
        print(f"True!, {m} is a perfect number.")
    else:
        print(f"True!, {m} is not a perfect number.")


perfect_integer(6)
perfect_integer(8)
perfect_integer(28)
