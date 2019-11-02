import time
print("DAY OF THE WEEK CALCULATOR")
print("--------------------------")
date = input("Give me a date (MM/DD/YYYY): ")
month = int(date[0:-8])
year2 = int(date[6:])
if month < 3:
    month = month+12
    year2 = year2-1
day = int(date[3:-5])
year = year2%100
century = year2//100
a = int(13*(month+1)/5)
b = int(year/4)
c = int(century/4)
dow = (day+a+year+b+c+5*century)%7
print("\nThat date falls on a ", end='')
if dow == 0:
    print("Saturday")
if dow == 1:
    print("Sunday")
if dow == 2:
    print("Monday")
if dow == 3:
    print("Tuesday")
if dow == 4:
    print("Wednesday")
if dow == 5:
    print("Thursday")
if dow == 6:
    print("Friday")

input()