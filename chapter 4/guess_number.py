import random
def guess_number():
	number_guess = random.randint(1, 1000)
	attempt = 0
	while True:

		guess = int(input("guess a number between 1 and 1000 with fewest guesses:"))
		if guess < number_guess:
			print("Too low. Try again")
		elif guess > number_guess:
			print("Too high. Try again")
		else:
			print("congratulations.You guessed the number! {number_guess} in {attempt} attempts")



print(guess_number())