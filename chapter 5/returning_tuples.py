def rotate(name, number, value):
    return (value, name, number)

name = 'Doug'
number = 22
value = 1984
name, number, value = rotate(name, number, value)
print(name, number, value)
name, number, value = rotate(name, number, value)
print(name, number, value)
name, number, value = rotate(name, number, value)
print(name, number, value)
