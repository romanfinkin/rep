def make_turn(field, x, y, value):

    if field[x][y] == ' ':
        field[x][y] = value
        result = True
    else:
        result = False

    return result
