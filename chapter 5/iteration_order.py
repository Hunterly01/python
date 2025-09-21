lst = [[0,0,0], [0,0,0]]
number = 1
for count in range(len(lst)):
    for counter in range(3):
        lst[count][counter] = number
        number += 1

print(lst)

