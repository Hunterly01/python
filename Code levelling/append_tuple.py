def append_number_in_tuple(one_tuple, number):
	if not one_tuple:
		raise ValueError("Empty tuple");
	new_tuple = list(one_tuple)
	new_tuple.append(number)
	return tuple(new_tuple)

	