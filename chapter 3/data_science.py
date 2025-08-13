numbers = [9, 11, 17, 22, 22, 22, 34, 34, 40] 
	  

sum = 0
mean = 0
for digit in numbers:
	sum += digit

mean = sum/9
mode = 22
median = numbers[4]

print("mean is ", mean)
print("mode is ", mode)
print("median is ", mode)

print("The one with outliers next ")
another_numbers = [9, 11, 17, 22, 22, 22, 34, 34, 34, 40] 
	  

sum1 = 0
mean1 = 0
for digit in another_numbers:
	sum += digit

mean1 = sum/10
mode1 = 22
median1 = another_numbers[4] / another_numbers[5]

print("mean  is ", mean1)
print("mode is ", mode1)
print("median is ", median1)