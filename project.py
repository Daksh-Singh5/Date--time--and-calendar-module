import calendar
year=int(input("Which year calender do u want to see: "))
month=input("do u want to to see a month: ")
if month=="yes":
    month=int(input("Which one: "))
    print(calendar.month(year,month))
else:
    month=0
    print(calendar.calendar(year))

