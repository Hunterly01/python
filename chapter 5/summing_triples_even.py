numbers = list(range(1, 11))
total = sum([count * 3 for count in numbers if count % 2 == 0])
print(total)