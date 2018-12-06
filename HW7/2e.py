from re import fullmatch

positive = ['bar', 'car', 'far', 'war', '0ar', '$ar']
negative = ['bag', 'for', 'star', 'care']

for x in positive + negative:
    match = fullmatch('(b|c|f|w|0|\W)ar', x)
    if match:
        print(x, match, match.group(0), match.group(1))
    else:
        print(x, None)
