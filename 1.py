def if_function(condition, true_result, false_result):
    if condition:
        return true_func(true_result)
    else:
        return false_func(false_result)


def true_func(true_result):
    return true_result


def false_func(false_result):
    return false_result


def main():
    print(if_function(False, 1, 3))


main()
