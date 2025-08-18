def change_third_element_element_second_value(tuple_list, number):
	if not tuple_list:
		return ValueError("empty tuple")
	tuple_list[2][1] = number
	return tuple_list