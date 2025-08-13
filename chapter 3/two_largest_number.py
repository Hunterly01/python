numberone = int(input("Enter an integer:"))
largest = numberone
smallest = numberone
secondLargest = numberone;
for count in range(9):
	number = int(input("Enter an integer:"))
	if(number > largest):
		largest = number
	if(number < smallest):
		smallest = number
		
print(largest)
print(smallest)


	