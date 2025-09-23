def check_even_number(number):
	return number % 2 != 0

def is_even_number(number):
	if number == 0:
		raise ValueError("Invalid input")
	if type(number) == str:
		raise ValueError("Invalid ")

	return list(filter(check_even_number,number))





numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(is_even_number(numbers))	