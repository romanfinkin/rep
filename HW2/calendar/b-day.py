import calendar

calendar.setfirstweekday(calendar.MONDAY)

bd = input('Enter date of your b-day ')

bdl = [bd[0:2], bd[3:5], bd[6:10]]

#print(bdl)

dd = int(bdl[0])
mm = int(bdl[1])
yyyy = int(bdl[2])


if calendar.weekday(yyyy, mm, dd) == 0:
    print("It's MONDAY")
elif calendar.weekday(yyyy, mm, dd) == 1:
    print("It's TUESDAY")
elif calendar.weekday(yyyy, mm, dd) == 2:
    print("It's WEDNESDAY")
elif calendar.weekday(yyyy, mm, dd) == 3:
    print("It's THURSDAY")
elif calendar.weekday(yyyy, mm, dd) == 4:
    print("It's FRIDAY")
elif calendar.weekday(yyyy, mm, dd) == 5:
    print("It's SATURDAY")
elif calendar.weekday(yyyy, mm, dd) == 6:
    print("It's SUNDAY")
