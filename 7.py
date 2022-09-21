def same_ord(a, b):
    len_of_a = len(str(a))
    len_of_b = len(str(b))
    print(f"Digits of first number is {len_of_a} and digits of second number is {len_of_b}.")
    if len_of_a == len_of_b:
        print("True")
    else:
        print("False")


same_ord(50, 100)
same_ord(50, 70)
same_ord(1000, 100000)
