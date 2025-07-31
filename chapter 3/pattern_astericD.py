for row in range (1,11):
	for space in range(11 - row):
		print(' ', end=' ')
	for asteric in range(1, row + 1):
		print('*',end=' ')

	print()

