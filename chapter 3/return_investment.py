principal = int(input("Enter the principal:"))
rate = int(input("Enter the rate:"))

for year in range(1, 31):   
	amount = principal * (1 + rate) ** year 
	print(f'{year:>2}{amount:>10.2f}')