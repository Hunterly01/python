def get_length(list):
	if list  == 0:
		raise ValueError("invalid")
	if list < 0:
		raise ValueError("invalid")
	return list




words = ["apple", "banana", "cherry"]
print(list(map(len,words)))