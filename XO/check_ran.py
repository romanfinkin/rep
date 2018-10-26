def check_range(field, x, y):
    if 0 <= x <= 3 and 0 <= y <= 3 and field[x][y] == ' ':
        result = True
    else:
        result = False
    return result

