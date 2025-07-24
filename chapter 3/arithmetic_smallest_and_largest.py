numberone = int(input("Enter an integer:"))
largest = numberone
smallest = numberone
sum = numberone
product = numberone
average = 0 

for count in range(3):
	number = int(input("Enter an integer:"))
	sum += number
	product *= number
	average = sum / 4

	if(number > largest):
		largest = number
	if(number < smallest):
		smallest = number
print("sum is ", sum)
print("product is ", product)
print("average is ", average)
print("largest number is ", largest)
print("smallest number is ", smallest)

