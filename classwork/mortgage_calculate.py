principal_amount = int(input("Enter the principal amount:"))
annual_rate = int(input("Enter the annual rate:"))
duration = int(input("Enter the duration of loan:"))
PERCENTAGE = 100
MONTH_IN_YEAR = 12
monthly_rate = annual_rate /PERCENTAGE / MONTH_IN_YEAR

duration_month = duration * MONTH_IN_YEAR 
numerator = monthly_rate * ((1  +  monthly_rate) ** duration_month)
denominator = ((1  +  monthly_rate) ** duration_month) - 1

monthly_payment = principal_amount * (numerator / denominator) 


print("The monthly payment is ", monthly_payment)