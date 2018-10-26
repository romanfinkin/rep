import math

a = int(input('First number '))
b = int(input('Second number '))
c = int(input('Third number '))


if a + b > c and b + c > a and a + c > b:
    print('All OK')
    cosA = (b ** 2 + c ** 2 - a ** 2) / 2 * b * c
    Y1 = math.acos((b ** 2 + c ** 2 - a ** 2) / 2 * b * c)
    print(math.degrees(Y1))
else:
    print('NOT GOOD')

math.ac
