from functools import reduce
import random

while True:
    try:
        n = int(input('Enter number '))
        print('Nice job, you seq - >')
        break
    except ValueError:
        print('Try again, you can input only numbers ')


lst = []


for i in range(n):
    lst.append(random.randrange(1, 10))

print(lst)
print('')

print('Now you must select one operation from each string and write them through the whitespace')
print('')

def join(x, y):
    return 10 * x + y


s_union = set()
s_union.add(lst[0])


def union(x, y):
    s_union.add(y)
    return s_union


rev_seq = [lst[0]]


def reverse(x, y):
    rev_seq.insert(0, y)
    return rev_seq


def simples(x):
    return x in {1, 2, 3, 5, 7}


reducers = {'sum': lambda x, y: x + y, 'multiply': lambda x, y: x * y, 'join': join, 'union': union,
            'reverse': reverse}
mappers = {'negated': lambda x: -x, 'inverted': lambda x: 1 / x, 'squared': lambda x: x * x}
predicates = {'evens': lambda x: x % 2 == 0, 'odds': lambda x: (x % 2) == 1, 'simples': simples}

while True:
    try:
        print('1. sum, multiply, join, unite, reverse')
        print('2. negated, inverted, squared')
        print('3. odds, evens, simple')
        print('')
        operation = str(input())
        oper1, oper2, oper3 = operation.split()
        reducer = reducers[oper1]
        mapper = mappers[oper2]
        predicate = predicates[oper3]
        break
    except ValueError:
        print('Almost try one more time')
        print('')
    except KeyError:
        print('Almost try one more time')
        print('')


result = reduce(reducer, map(mapper, filter(predicate, lst)))
print(result)
