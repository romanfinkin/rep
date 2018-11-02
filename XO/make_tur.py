def make_turn(field, x, y, value):
    # немного напутал :)
    # ты проверку field[x][y] == ' ' унес в check_range, а она должна была быть тут
    field[x][y] = value
    result = True
    return result
