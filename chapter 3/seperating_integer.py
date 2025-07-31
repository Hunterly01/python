number = int(input("Enter five digit number:"))

digit1 = number // 10000
digit2 = (number // 1000) % 10
digit3 = (number // 100) % 10
digit4 = (number // 10) % 10
digit5 = number % 10

print(digit1)
print(digit2)
print(digit3)
print(digit4)
print(digit5)
