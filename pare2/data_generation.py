import random
from not_null_field import not_null_field

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
    [['1X1'], ['1X2'], ['1X3'], ['1X4'], ['1X5'], ['1X6'], ['1X7'], ['1X8'], ['1X9']],
    [['X'], ['X'], ['X'], ['X'], ['X'], ['X'], ['X'], ['X'], ['X']],
    [['X'], ['X'], ['X'], ['X'], ['X'], ['X'], ['X'], ['X'], ['X']],
    [['X'], ['X'], ['X'], ['X'], ['X'], ['X'], ['X'], ['X'], ['X']]
]


def data_generation(cards_arr, arr_data):
    try:
        while not_null_field(arr_data) is True:
            i = 0
            j = 0
            while j < 9:
                rand_card_numb = random.randrange(0, 36)
                card = cards_arr[rand_card_numb]
                while arr_data[i][j] == ['X']:
                    if card == 'X':
                        break
                    else:
                        arr_data[i][j] = card
                        cards_arr[rand_card_numb] = 'X'
                        j += 1
                        if j == 9 and i <= 3:
                            i += 1
                            j = 0
                        break
    except(IndexError):
        pass



data_generation(cards, data)
