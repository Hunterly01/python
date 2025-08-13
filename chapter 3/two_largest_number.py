
largest = 0;
secondLargest = 0;
for count in range(10):
	number = int(input("Enter an integer:"))
	if(number > largest):
		secondLargest = largest
		largest = number
	elif number > secondLargest and largest != number:
		secondLargest = number
		
print(largest)
print(secondLargest)


