str1 = ''
while str1 == '':
    str1 = input('Input string ')

part_lens_str1 = len(str1) // 2
lens_str1 = len(str1)
if len(str1) % 2 != 0:
    part_lens_str1 += 1

#print(part_lens_str1)

#print(range(part_lens_str1))

for letter in range(part_lens_str1):
    #print(letter)
    if str1[letter] == str1[-1 - letter]:
        if letter == part_lens_str1 - 1:
            print('Correctly')
    else:
        print('Incorrectly')
        break

