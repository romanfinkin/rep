def check_field(field, value):
    def check_rows(field, value):
        for i in range(2):
            if field[i][0] == field[i][1] == field[i][2] == value:
                result_rows = True
            else:
                result_rows = False

        return result_rows

    def check_cols(field, value):
        for j in range(2):
            if field[0][j] == field[1][j] == field[2][j] == value:
                result_cols = True
            else:
                result_cols = False

        return result_cols

    def check_diagonals(field, value):
        if field[0][0] == field[1][1] == field[2][2] == value or field[0][2] == field[1][1] == field[2][0]:
            result_diagonals = True
        else:
            result_diagonals = False

        return result_diagonals
