from data_generation import *
from print_field import *
from re import *

cards = [
    '6♣ ', '7♣ ', '8♣ ', '9♣ ', '10♣', 'J♣ ', 'Q♣ ', 'K♣ ', 'A♣ ',
    '6♦ ', '7♦ ', '8♦ ', '9♦ ', '10♦', 'J♦ ', 'Q♦ ', 'K♦ ', 'A♦ ',
    '6♥ ', '7♥ ', '8♥ ', '9♥ ', '10♥', 'J♥ ', 'Q♥ ', 'K♥ ', 'A♥ ',
    '6♠ ', '7♠ ', '8♠ ', '9♠ ', '10♠', 'J♠ ', 'Q♠ ', 'K♠ ', 'A♠ '
]

data = [
    [['X'], ['X'], ['X'], ['X'], ['X'], ['X'], ['X'], ['X'], ['X']],
    [['X'], ['X'], ['X'], ['X'], ['X'], ['X'], ['X'], ['X'], ['X']],
    [['X'], ['X'], ['X'], ['X'], ['X'], ['X'], ['X'], ['X'], ['X']],
    [['X'], ['X'], ['X'], ['X'], ['X'], ['X'], ['X'], ['X'], ['X']]
]

field = [
    [['X'], ['X'], ['X'], ['X'], ['X'], ['X'], ['X'], ['X'], ['X']],
    [['X'], ['X'], ['X'], ['X'], ['X'], ['X'], ['X'], ['X'], ['X']],
    [['X'], ['X'], ['X'], ['X'], ['X'], ['X'], ['X'], ['X'], ['X']],
    [['X'], ['X'], ['X'], ['X'], ['X'], ['X'], ['X'], ['X'], ['X']]
]

win = [
    [[' '], [' '], [' '], [' '], [' '], [' '], [' '], [' '], [' ']],
    [[' '], [' '], [' '], [' '], [' '], [' '], [' '], [' '], [' ']],
    [[' '], [' '], [' '], [' '], [' '], [' '], [' '], [' '], [' ']],
    [[' '], [' '], [' '], [' '], [' '], [' '], [' '], [' '], [' ']]
]

data_generation(cards, data)

for i in range(9):
    field[3][i] = data[3][i]

end_count = 0

while True:

    for i in range(len(field)):
        print(field[i])

    rows = [3, 2, 1, 0]

    first_position = int(input('Enter first position -> '))
    first_position -= 1
    fp = int(first_position)

    t1 = 0
    for i in rows:
        first_card = field[i][first_position][0]
        if first_card != ' ':
            t1 = int(i)
            print(field[i][first_position])
            break
        else:
            continue

    first_card = str(field[t1][first_position])

    second_position = int(input('Enter second position - > '))
    second_position -= 1
    sp = int(second_position)

    t2 = 0
    for i in rows:
        second_card = field[i][second_position][0]
        if second_card != ' ':
            t2 = int(i)
            print(field[i][second_position])
            break
        else:
            continue

    second_card = str(field[t2][second_position])

    if str(field[t2][second_position][0]) == str(field[t1][first_position][0]):
        print('\n')
        print('\n')
        print('\n')
        print('\n')
        print('\n')
        print('\n')
        print('\n')
        print('Good! Make new turn!')
        field[t1][fp] = [' ']
        field[t2][sp] = [' ']
        if field[0][fp] == field[1][fp] == field[2][fp] == field[3][fp]:
            field[t2 - 1][sp] = data[t2 - 1][sp]
            continue
        elif field[0][sp] == field[1][sp] == field[2][sp] == field[3][sp]:
            field[t1 - 1][fp] = data[t1 - 1][fp]
            continue
        elif field[0][fp] == field[1][fp] == field[2][fp] == field[3][fp] and field[0][sp] == field[1][sp] == field[2][sp] == field[3][sp]:
            continue
        else:
            field[t1 - 1][fp] = data[t1 - 1][fp]
            field[t2 - 1][sp] = data[t2 - 1][sp]
        if field == win:
            print('\n')
            print('\n')
            print('\n')
            print('\n')
            print('\n')
            print('\n')
            print('\n')
            print("Perfect! It's a WINNER!")

    else:
        print('\n')
        print('\n')
        print('\n')
        print('\n')
        print('\n')
        print('\n')
        print('\n')
        end_count += 1
        if end_count < 3:
            print('Try again')
        elif end_count == 3:
            print("it's end of your game!")
            break
        else:
            continue
