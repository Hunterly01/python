def sum_inner_two_d_list_index(lst):
	if not lst:
		raise ValueError("Empty list")
	answer = [0] * len(lst[0])
	for inner_lst in lst:
		for index in range(len(inner_lst)):
			answer[index] += inner_lst[index]
	return answer