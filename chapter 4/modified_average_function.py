def average(number, *args):
	if number and args == 0:
		return "Error"
	total = number + sum(args)
	count = len(args) + 1
	return  total / count 

print(average(1, 2, 3, 4))