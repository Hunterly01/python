number1 = int(input("Enter a number:"))
largest = number1
second_largest = number1
for count in range (1,10):
	number = int(input("Enter a number:"))
	if number > largest:
		second_largest = largest
		largest = number
	elif number > second_largest:
		second_largest = number
print("largest is ", largest, " and second largest is ", second_largest)