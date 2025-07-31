
while True:
	
	gallons_used = float(input("Enter the gallons used (-1 to end):"))
	if gallons_used == -1:
		print("stop")
		break

	miles_driven =  float(input("Enter the miles driven:"))
	miles_per_gallon = miles_driven / gallons_used
	print(f"The miles per gallon used for this tank was {miles_per_gallon: 10.2f} ")






