from functools import reduce
def add(number , value):
	return number + value



def reduce_sum():
	return reduce(add, range(1, 51))