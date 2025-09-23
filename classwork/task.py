import math
def get_student_square(numbers):
	if not numbers:
		raise ValueError("Empty list")
	new_list = []
	for number in numbers:
		if number % math.sqrt(number) == 0:
			new_list.append(True)
		else:
			new_list.append(False)
			
	return new_list



numberT = [2,3,4,5,6,7,16]
print(get_student_square(numberT))






			