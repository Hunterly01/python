number = int(input("Enter five digit number:"))

digit1 = number // 10000
digit2 = (number // 1000) % 10
digit4 = (number // 10) % 10
digit5 = number % 10

if (digit1 == digit5 and digit2 == digit4):
	print (number, " is a palindrome")
else:
	print (number, " is not a palindrome")

