def get_number(number):
	return number % 3 == 0 and number % 5 == 0



def filter_to_get_all_number():
	return list(filter(get_number, range(1, 51)))