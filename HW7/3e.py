from re import fullmatch

positive = ['rock', 'core', 'roar', 'doors', 'looolz']
negative = ['hog', 'rack', 'shock', 'pocket']

for x in positive + negative:
    match = fullmatch('(r|c|d|l)(o+)(c|r|a|l)(k|e|r|s|z)', x)
    if match:
        print(x, match, match.group(0), match.group(1))
    else:
        print(x, None)
