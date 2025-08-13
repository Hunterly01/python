total = 1
factorial = 1
for number in range(1, 11):
	factorial = factorial * number
	total =  total + (1/factorial)
print(f"{total:.2f}") 
print(round(total,2)) 