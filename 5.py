def largest_integer(m):
    factorials = []
    for i in range(1, m):
        if m % i == 0:
            factorials.append(i)
    print(f"List of Factorials for {m} are {factorials}")
    print("Largest factor is: " + str(factorials[-1]))


largest_integer(15)
largest_integer(80)
