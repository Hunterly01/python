def is_odd(number):
    print("filtering", number)
    return number % 2 == 1

def square(number):
    print("mapping", number)
    return number * number

numbers = [2, 3, 4, 5, 9]
result = list(map(square, filter(is_odd, numbers)))

answer = list(filter(is_odd, map(square, numbers)))
print(result)
print(answer)