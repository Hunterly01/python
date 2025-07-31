for row in range (1,11):
	for asteric in range(1,row + 1):
		print('*',end=' ')
	print()








for row in range (11, 0, -1):
	for asteric in range(1,row - 1):
		print('*',end=' ')

	print()





for row in range (1,11):
	for space in range(11 - row):
		print(' ', end=' ')
	for asteric in range(1, row + 1):
		print('*',end=' ')

	print()

