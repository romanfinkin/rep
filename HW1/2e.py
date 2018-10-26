number_str = input('Enter quantity of number ')
number_int = int(number_str)

i = 0
number_sum = 0

for i in range(number_int):
    x_str = input('№%d -> ' % int(i+1))
    x_int = int(x_str)
    if x_int % 3 == 0:
        number_sum = number_sum + x_int

print('Sum = %d' % number_sum)
