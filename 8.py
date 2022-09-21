def double_5(num):
    number = str(num)
    contains_55 = "55"
    if contains_55 in number:
        print(f"True! 55 is in {number}")
    else:
        print("False!")


double_5(5055055)
double_5(55)
double_5(50505050)
