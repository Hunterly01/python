def get_first_tuple_greater_than_two(lst):
	return lst[0] > 2


def fiter_tuple(information):
	return list(filter(get_first_tuple_greater_than_two, information))