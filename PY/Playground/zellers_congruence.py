# the better version
def zellers_congruence(month, day, year):
    if month < 3:
        month += 12
        year -= 1

    year_of_century = year%100
    zb_century = year//100

    index = (day + 13*(month + 1)//5 + year_of_century + year_of_century//4 + zb_century//4 + 5*zb_century) % 7
    return ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'][index]

def main():
    print("Enter a date (MM/DD/YYYY)")
    month, day, year = list(map(int, input('> ').split('/')))
    print()
    print('That date falls on a ' + zellers_congruence(month, day, year))

if __name__ == '__main__':
     main()
