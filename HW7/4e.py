from re import fullmatch

value = ['1', '-23', '1231231', '456.789', 'hello!']

for x in value:
    match = fullmatch('(\d*?)(\W|\d)(\d*?)', x)
    if match:
        print(x, match, match.group(0), match.group(1))
    else:
        print(x, None)
