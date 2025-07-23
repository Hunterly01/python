
print("""
	1.Monday
	2.Tuesday
	3.Wednesday
	4.Thurday
	5.Friday
	6.Saturday
	7.Sunday
	""")

print("Enter an option from 1 to 7:")
n = int(input("Enter number of day:"))
match(n):
	case 1:
		print("Monday")
	case 2:
		print("Tuesday")
	case 3:
		print("wednesday")
	case 4:
		print("Thursday")
	case 5:
		print("Friday")
	case 6:
		print("Saturday")
	case 7:
		print("Sunday")
	case _:
		print("Exit")



