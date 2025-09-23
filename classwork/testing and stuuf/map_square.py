def squaresNumber(list):
	if list == 0:
		raise ValueError("invalid input");
	if type(list) == str:
		raise ValueError("invalid input");

	return list * list








numbers = [1, 2, 3, 4, 5];
print(list(map(squaresNumber,numbers)));

