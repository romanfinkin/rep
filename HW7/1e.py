from re import fullmatch

positive = ['dog', 'log', 'lock', 'dock']
negative = ['fog', 'block', 'locked']

for x in positive + negative:
    match = fullmatch('(l|d)o(g|ck)', x)
    if match:
        print(x, match, match.group(0), match.group(1))
    else:
        print(x, None)
