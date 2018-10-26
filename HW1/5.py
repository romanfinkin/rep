str1 = ''
str2 = ''
while str1 == '':
    str1 = input('Input first string ')
while str2 == '':
    str2 = input('Input Second string ')

if str2 in str1:
    print('Yes, second string part of first string')
else:
    print("No, second string is't part of first string")