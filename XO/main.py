list_a = ['-', '+', '-', '+', '-', '+', '-', '+']
list_b = [' ', '|', '1', '|', '2', '|', '3', '|']
list_1 = ['1', '|', ' ', '|', ' ', '|', ' ', '|']
list_2 = ['2', '|', ' ', '|', ' ', '|', ' ', '|']
list_3 = ['3', '|', ' ', '|', ' ', '|', ' ', '|']


def prnt():
    print('\n' * 100)
    print(list_b[0], list_b[1], list_b[2], list_b[3], list_b[4], list_b[5], list_b[6], list_b[7])
    print(list_a[0], list_a[1], list_a[2], list_a[3], list_a[4], list_a[5], list_a[6], list_a[7])
    print(list_1[0], list_1[1], list_1[2], list_1[3], list_1[4], list_1[5], list_1[6], list_1[7])
    print(list_a[0], list_a[1], list_a[2], list_a[3], list_a[4], list_a[5], list_a[6], list_a[7])
    print(list_2[0], list_2[1], list_2[2], list_2[3], list_2[4], list_2[5], list_2[6], list_2[7])
    print(list_a[0], list_a[1], list_a[2], list_a[3], list_a[4], list_a[5], list_a[6], list_a[7])
    print(list_3[0], list_3[1], list_3[2], list_3[3], list_3[4], list_3[5], list_3[6], list_3[7])
    print(list_a[0], list_a[1], list_a[2], list_a[3], list_a[4], list_a[5], list_a[6], list_a[7])
    return 0




player = 1
for i in range(9):
    if list_1[2] == list_1[4] == list_1[6] == 'X':
        prnt()
        print('X just Win!!!')
        break
    elif list_2[2] == list_2[4] == list_2[6] == 'X':
        prnt()
        print('X just Win!!!')
        break
    elif list_3[2] == list_3[4] == list_3[6] == 'X':
        prnt()
        print('X just Win!!!')
        break
    elif list_1[2] == list_1[2] == list_3[2] == 'X':
        prnt()
        print('X just Win!!!')
        break
    elif list_1[4] == list_2[4] == list_3[4] == 'X':
        prnt()
        print('X just Win!!!')
        break
    elif list_1[6] == list_2[6] == list_3[6] == 'X':
        prnt()
        print('X just Win!!!')
        break
    elif list_1[2] == list_2[4] == list_3[6] == 'X':
        prnt()
        print('X just Win!!!')
        break
    elif list_1[6] == list_2[4] == list_3[2] == 'X':
        prnt()
        print('X just Win!!!')
        break

    if list_1[2] == list_1[4] == list_1[6] == 'O':
        prnt()
        print('X just Win!!!')
        break
    elif list_2[2] == list_2[4] == list_2[6] == 'O':
        prnt()
        print('X just Win!!!')
        break
    elif list_3[2] == list_3[4] == list_3[6] == 'O':
        prnt()
        print('X just Win!!!')
        break
    elif list_1[2] == list_1[2] == list_3[2] == 'O':
        prnt()
        print('X just Win!!!')
        break
    elif list_1[4] == list_2[4] == list_3[4] == 'O':
        prnt()
        print('X just Win!!!')
        break
    elif list_1[6] == list_2[6] == list_3[6] == 'O':
        prnt()
        print('X just Win!!!')
        break
    elif list_1[2] == list_2[4] == list_3[6] == 'O':
        prnt()
        print('X just Win!!!')
        break
    elif list_1[6] == list_2[4] == list_3[2] == 'O':
        prnt()
        print('X just Win!!!')
        break
    else:
        prnt()
        if player % 2 == 1:
            print('Player 1')
            x = int(input('Enter number of line '))
            y = int(input('Enter number of column '))
            if player % 2 == 1:
                if x == 1:
                    if y == 1:
                        if list_1[2] == ' ':
                            list_1[2] = 'X'
                        else:
                            print('Cell busy')
                            player -= 1
                    if y == 2:
                        if list_1[4] == ' ':
                            list_1[4] = 'X'
                        else:
                            print('Cell busy')
                            player -= 1
                    if y == 3:
                        if list_1[6] == ' ':
                            list_1[6] = 'X'
                        else:
                            print('Cell busy')
                            player -= 1
                    player += 1
                elif x == 2:
                    if y == 1:
                        if list_2[2] == ' ':
                            list_2[2] = 'X'
                        else:
                            print('Cell busy')
                            player -= 1
                    if y == 2:
                        if list_2[4] == ' ':
                            list_2[4] = 'X'
                        else:
                            print('Cell busy')
                            player -= 1
                    if y == 3:
                        if list_2[6] == ' ':
                            list_2[6] = 'X'
                        else:
                            print('Cell busy')
                            player -= 1
                    player += 1
                elif x == 3:
                    if y == 1:
                        if list_3[2] == ' ':
                            list_3[2] = 'X'
                        else:
                            print('Cell busy')
                            player -= 1
                    if y == 2:
                        if list_3[4] == ' ':
                            list_3[4] = 'X'
                        else:
                            print('Cell busy')
                            player -= 1
                    if y == 3:
                        if list_3[6] == ' ':
                            list_3[6] = 'X'
                        else:
                            print('Cell busy')
                            player -= 1
                    player += 1
                else:
                    print('Wrong number, try again ')
            elif player % 2 == 0:
                if x == 1:
                    if y == 1:
                        if list_1[2] == ' ':
                            list_1[2] = 'O'
                        else:
                            print('Cell busy')
                            player -= 1
                    if y == 2:
                        if list_1[4] == ' ':
                            list_1[4] = 'O'
                        else:
                            print('Cell busy')
                            player -= 1
                    if y == 3:
                        if list_1[6] == ' ':
                            list_1[6] = 'O'
                        else:
                            print('Cell busy')
                            player -= 1
                    player += 1
                elif x == 2:
                    if y == 1:
                        if list_2[2] == ' ':
                            list_2[2] = 'O'
                        else:
                            print('Cell busy')
                            player -= 1
                    if y == 2:
                        if list_2[4] == ' ':
                            list_2[4] = 'O'
                        else:
                            print('Cell busy')
                            player -= 1
                    if y == 3:
                        if list_2[6] == ' ':
                            list_2[6] = 'O'
                        else:
                            print('Cell busy')
                            player -= 1
                    player += 1
                elif x == 3:
                    if y == 1:
                        if list_3[2] == ' ':
                            list_3[2] = 'O'
                        else:
                            print('Cell busy')
                            player -= 1
                    if y == 2:
                        if list_3[4] == ' ':
                            list_3[4] = 'O'
                        else:
                            print('Cell busy')
                            player -= 1
                    if y == 3:
                        if list_3[6] == ' ':
                            list_3[6] = 'O'
                        else:
                            print('Cell busy')
                            player -= 1
                    player += 1
                else:
                    print('Wrong number, try again ')
        else:
            print('Player 2')
            x = int(input('Enter number of line '))
            y = int(input('Enter number of column '))
            if player % 2 == 1:
                if x == 1:
                    if y == 1:
                        if list_1[2] == ' ':
                            list_1[2] = 'X'
                        else:
                            print('Cell busy')
                            player -= 1
                    if y == 2:
                        if list_1[4] == ' ':
                            list_1[4] = 'X'
                        else:
                            print('Cell busy')
                            player -= 1
                    if y == 3:
                        if list_1[6] == ' ':
                            list_1[6] = 'X'
                        else:
                            print('Cell busy')
                            player -= 1
                    player += 1
                elif x == 2:
                    if y == 1:
                        if list_2[2] == ' ':
                            list_2[2] = 'X'
                        else:
                            print('Cell busy')
                            player -= 1
                    if y == 2:
                        if list_2[4] == ' ':
                            list_2[4] = 'X'
                        else:
                            print('Cell busy')
                            player -= 1
                    if y == 3:
                        if list_2[6] == ' ':
                            list_2[6] = 'X'
                        else:
                            print('Cell busy')
                            player -= 1
                    player += 1
                elif x == 3:
                    if y == 1:
                        if list_3[2] == ' ':
                            list_3[2] = 'X'
                        else:
                            print('Cell busy')
                            player -= 1
                    if y == 2:
                        if list_3[4] == ' ':
                            list_3[4] = 'X'
                        else:
                            print('Cell busy')
                            player -= 1
                    if y == 3:
                        if list_3[6] == ' ':
                            list_3[6] = 'X'
                        else:
                            print('Cell busy')
                            player -= 1
                    player += 1
                else:
                    print('Wrong number, try again ')
            elif player % 2 == 0:
                if x == 1:
                    if y == 1:
                        if list_1[2] == ' ':
                            list_1[2] = 'O'
                        else:
                            print('Cell busy')
                            player -= 1
                    if y == 2:
                        if list_1[4] == ' ':
                            list_1[4] = 'O'
                        else:
                            print('Cell busy')
                            player -= 1
                    if y == 3:
                        if list_1[6] == ' ':
                            list_1[6] = 'O'
                        else:
                            print('Cell busy')
                            player -= 1
                    player += 1
                elif x == 2:
                    if y == 1:
                        if list_2[2] == ' ':
                            list_2[2] = 'O'
                        else:
                            print('Cell busy')
                            player -= 1
                    if y == 2:
                        if list_2[4] == ' ':
                            list_2[4] = 'O'
                        else:
                            print('Cell busy')
                            player -= 1
                    if y == 3:
                        if list_2[6] == ' ':
                            list_2[6] = 'O'
                        else:
                            print('Cell busy')
                            player -= 1
                    player += 1
                elif x == 3:
                    if y == 1:
                        if list_3[2] == ' ':
                            list_3[2] = 'O'
                        else:
                            print('Cell busy')
                            player -= 1
                    if y == 2:
                        if list_3[4] == ' ':
                            list_3[4] = 'O'
                        else:
                            print('Cell busy')
                            player -= 1
                    if y == 3:
                        if list_3[6] == ' ':
                            list_3[6] = 'O'
                        else:
                            print('Cell busy')
                            player -= 1
                    player += 1
                else:
                    print('Wrong number, try again! ')
