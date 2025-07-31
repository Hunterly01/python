import math
def get_divide_or_square(number):
	if  type(number) == float:
		raise ValueError
	if int(number) < 0:
		raise ValueError 
	if  type(number) == str:
		raise ValueError
	if number % 5 == 0:
		result = math.sqrt(number)
		return result
	if number % 5 != 0:
		result = float(number)
		return result
	
	
		
		
def get_future_amount(investment_amount, monthly_interestRate, years):
	if type(investment_amount) == float:
		raise ValueError
	if type(investment_amount) == str:
		raise ValueError
	if int(monthly_interestRate) < 0:
		raise ValueError
	future_amount = investment_amount + (1 + monthly_interestRate) ** years
	return future_amount



	

