def unpack_tuple_into_variables(numbers):
	if not numbers:
		raise ValueError("empty tuple")
	a, b, *last = numbers
	return a, b, last


