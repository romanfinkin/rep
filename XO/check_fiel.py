def check_field(field, value):
    result = False
    for i in range(2):
        if field[i][0] == field[i][1] == field[i][2] == value != ' ':
            print('%s Wins' % value)
            result = True

    for j in range(2):
        if field[0][j] == field[1][j] == field[2][j] == value != ' ':
            print('%s Wins' % value)
            result = True

    if field[0][0] == field[1][1] == field[2][2] == value != ' ' or field[0][2] == field[1][1] == field[2][0] != ' ':
        print('%s Wins' % value)
        result = True
    return result