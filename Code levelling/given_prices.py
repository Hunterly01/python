def check_given_prices(number):
	return round(number * 1.10, 3)


def add_percentage_to_price(lst):
	return list(map(check_given_prices, lst))

