def convert_tuple_to_list(fruits, fruit):
	if not fruits:
		raise ValueError("Empty tuple")
	list_fruit = list(fruit)
	list_fruit.append(fruit);
	return tuple(list_fruit)