firstNumber = int(input("Enter first number:"))
secondNumber = int(input("Enter second number:"))
thirdNumber = int(input("Enter third number:"))


sum = firstNumber + secondNumber + thirdNumber
print("Sum of numbers ", sum)

product = firstNumber * secondNumber * thirdNumber
print("product of numbers ", product)

Average = firstNumber + secondNumber + thirdNumber / 3
print("Average of numbers ", Average)



largest = firstNumber
smallest =  firstNumber

if(secondNumber < smallest):smallest = secondNumber
if(thirdNumber < smallest):smallest = thirdNumber
print("The smallest number is ", smallest)

if(secondNumber > largest):largest = secondNumber
if(thirdNumber > largest):largest = thirdNumber
print("The largest number is ", largest)











