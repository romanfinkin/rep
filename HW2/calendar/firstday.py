import calendar

calendar.setfirstweekday(calendar.MONDAY)

dow = input('Enter day of week ')

dow_int = 0

if dow == 'Monday':
    dow_int = 0
elif dow == 'Tuesday':
    dow_int = 1
elif dow == 'Wednesday':
    dow_int = 2
elif dow == 'Thursday':
    dow_int = 3
elif dow == 'Friday':
    dow_int = 4
elif dow == 'Saturday':
    dow_int = 5
elif dow == 'Sunday':
    dow_int = 6

i = 11
for year in range(2018, 3000):
    for month in range(11, 100):
        if month % 12 == 0:
            m = 12
        else:
            m = month % 12
        if calendar.monthrange(year, m) == dow_int:
            print(dow_int)