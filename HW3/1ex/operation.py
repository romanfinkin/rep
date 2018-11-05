from main import lst
from functools import reduce


def join(seq: list):
    j = 1
    res = 0
    y = 0
    for i in seq:
        y = i * (10 ** (len(seq) - j))
        res = res + y
        j += 1
    return res


oper_map1 = {'sum': reduce(lambda x, y: x + y, lst), 'multiply': reduce(lambda x, y: x * y, lst), 'join': join(lst)}

