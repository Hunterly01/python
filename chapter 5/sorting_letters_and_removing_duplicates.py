import random

new_letters = []
count = 0
while count < 20:
    letter = random.choice("abcdef")
    new_letters.append(letter)
    count += 1

ascending = sorted(new_letters)
print(ascending)

decending = sorted(new_letters, reverse=True)
print(decending)

unique = sorted(set(new_letters))
print(unique)