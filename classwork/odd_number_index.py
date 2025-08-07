list = [2,3,4,5,6,7,8,9,10,11]
new_one = [];
for number in range(0,11):
	if number % 2 == 1:
		new_one.append(list[number]);
print(new_one);