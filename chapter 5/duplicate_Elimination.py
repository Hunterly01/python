def duplicate_Elimination(lst):
    new_lst = []
    for item in lst:
        if item not in new_lst:
            new_lst.append(item)
    new_lst.sort()
    return new_lst

array = [1, 2, 3, 4, 4, 6, 7, 9, 9, 10]
print(duplicate_Elimination(array))
letters = ['a', 'a', 'c', 'e', 'e', 'f', 'g', 'h', 'j', 'j']
print(duplicate_Elimination(letters))
