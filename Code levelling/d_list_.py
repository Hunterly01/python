def sum_dlist(lst):
	answer = []
	if not lst:
		raise ValueError("empty list")
	for inner_list in lst:
		sum = 0;
		for number in inner_list:
			sum += number
		answer.append(sum)
	return answer