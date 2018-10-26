import random

x = random.randrange(1, 10)
y = int(input('Enter option '))

while True:
    if x == y:
        print('Sucсess, you WIN!')
        break
    else:
        print('Not bad')
        y = int(input('Try again '))
