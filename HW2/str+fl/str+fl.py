import string


file = open('doc.txt')
text = file.read()
print(text)

j = 0

# Достаточно было посчитать пробелы
# Например, если у тебя строка "WordA. WordB. WordC." ты насчитаешь 5 слов, хотя тут только 3 слова.
for i in text:
    if i == ' ':
        j += 1
    elif i == '.':
        j += 1

print('Words in the text = %d' % j)
j = 0


#  Тут нужна провервка на то, что символ - это буква. Нужно ж было буквы посчитать, а не все символы.
d = dict.fromkeys(text, 0)
for i in text:
    d[i] += 1
print(d)

j = 1
for i in text:
    if i == "\n":
        j += 1

k = 0
fwr = open('res.txt', 'w')

for i in text:
    if i == '\n':
        k += 1
        if k <= j // 2:
            fwr.write(i)
fwr.close()

fwr = open('res.txt', 'r+')

k = 0
for i in text:
    if i == '\n':
        k += 1
        if k > j // 2:
            fwr.write(i)
fwr.close()
