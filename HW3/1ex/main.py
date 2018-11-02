import random

try:
    n = int(input('Enter number '))
except ValueError:
    n = int(input('Try again, you can input only numbers '))

lst = []
for i in range(n):
    lst.append(random.randrange(1, 10))

print(lst)
print('')

print('1. sum, multiply, join, unite, reverse')
print('2. negated, inverted, squared')
print('3. odds, evens, simple')

operation = str(input('Choose one operation from each item and enter them separated by a space: '))

op_lst = operation.split()
print(op_lst)

