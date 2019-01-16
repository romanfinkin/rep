from data_generation import data


def print_field(field):
    for i in range(9):
        field[3][i] = data[3][i]

    for i in range(len(field)):
        print(field[i])
