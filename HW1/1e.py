number_str = input('Enter number ')
number_int = int(number_str)

i = 0
j = 0

list_for_numbers = []

for i in number_str:
    list_for_numbers.append(number_str[j])
    j += 1

min_number = int(min(list_for_numbers))
max_number = int(max(list_for_numbers))

print('Minimal %d' % min_number)
print('Maximal %d' % max_number)







