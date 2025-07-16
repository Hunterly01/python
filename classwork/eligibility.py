age = int(input("Enter your age:"))
if age > 100:
 print("You are too old to vote")
elif (age >= 18 and age <= 100):
 print("You are eligible to vote")
else:
 print("You are too young to vote")
