import re

'''
Exceptions: 
[1518-05-31 23:59] Guard #2221 begins shift
[1518-04-30 23:59] Guard #2861 begins shift
[1518-09-30 23:56] Guard #2647 begins shift
'''

with open('guard_log.txt') as f:
    guard_log = f.read().split('\n')


guard_number = [entry for entry in guard_log if entry[-5:] == 'shift']
guard_log = [entry for entry in guard_log if entry[-5:] != 'shift']

date = re.compile(r'\d{4}-\d{2}-\d{2}')
time = re.compile(r'\d{2}:\d{2}')
number = re.compile(r'#(\d+)')


date_dictionary = {}

for entry in guard_log:
    date_ = date.search(entry).group(0)
    time_ = time.search(entry).group(0)
    event = entry[19]

    date_dictionary.setdefault(date_, [])
    date_dictionary[date_].append((time_, event))

guard_dictionary = {}

for entry in guard_number:
    date_ = date.search(entry).group(0)
    time_ = time.search(entry).group(0)
    number_ = number.search(entry).group(1)

    if time_[:2] == '23':
        if date_ == '1518-05-31':
            date_ = '1518-06-01'

        elif date_ == '1518-04-30':
            date_ = '1518-05-01'

        elif date_ == '1518-09-30':
            date_ = '1518-10-01'

        else:
            date_ = date_[:-2] + str(int(date_[-2:]) + 1).rjust(2, '0')

    guard_dictionary[date_] = number_

for time in date_dictionary:
    date_dictionary[time] = sorted(date_dictionary[time], key = lambda x: x[0][-2:])

time_dictionary = {}

for time in date_dictionary:
    guard = guard_dictionary[time]
    time_dictionary.setdefault(guard, {})

    while len(date_dictionary[time]) != 0:
        START = int(date_dictionary[time].pop(0)[0][-2:])
        END = int(date_dictionary[time].pop(0)[0][-2:])

        for minute in range(START, END):
            time_dictionary[guard].setdefault(minute, 0)
            time_dictionary[guard][minute] += 1

most_hours = (0, 0)
for guard in time_dictionary:
    total = 0
    for minute in time_dictionary[guard]:
        total += time_dictionary[guard][minute]
    if total > most_hours[1]:
        most_hours = (guard, total)

sleepiest_guard = most_hours[0]

most_slept_minute = sorted(time_dictionary[sleepiest_guard].items(), key = lambda x: x[1])[-1][0]

print("Sleepiest Guard: {}".format(sleepiest_guard))
print("Most slept minute: {}".format(most_slept_minute))
print(int(sleepiest_guard) * most_slept_minute)