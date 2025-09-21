def is_ordered(value):
    return value == sorted(value)


lst = [1, 2, 3, 4, 5, 9]
print(is_ordered(lst))
lst = [2, 1, 3, 4, 5, 9]
print(is_ordered(lst))