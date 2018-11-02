import pr_field
import check_fiel
import check_ran
import make_tur

data = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]
for i in range(9):
    if i % 2 == 0:
        value = 'X'
    else:
        value = 'O'
    pr_field.print_field(data)
    print('\n')
    x = int(input('Enter number of line '))
    x -= 1
    y = int(input('Enter number of column '))
    y -= 1
    while True:
        if check_ran.check_range(data, x, y):
            break
        else:
            print('Not right, try again ')
            x = int(input('Enter number of line '))
            y = int(input('Enter number of column '))
    make_tur.make_turn(data, x, y, value)
    if check_fiel.check_field(data, value) == True:
        # вывел бы хоть сообщение о том, кто победил :)
        break
