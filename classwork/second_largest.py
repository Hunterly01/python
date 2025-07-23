x = 42
y = 12
z = 55

if(x > z and x > y):
	if y > z:
		second_largest = y
	else:
		second_largest = z
elif(y > x and y > z):
	if y > z:
		second_largest = x
	else:
		second_largest = z
else:
	if y > z:
		second_largest = x
	else:
		second_largest = y
print(x, "is the second Highest score")
