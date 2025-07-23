for number in range (1, 51):
	if(number % 2 == 0):
		number = number * number
		print(number, end= ',')
	else:
		number = number **3
		print(number, end= ',')

