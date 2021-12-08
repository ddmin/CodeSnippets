# [Intermediate] Challenge 1

import os


clear = lambda : os.system('clear')


def print_events(events):
    if not events:
        print("No events yet!")
        return False

    for event in events:
        print("(" + str(event[1]).zfill(2) + ":" + str(event[2]).zfill(2) + ") - " + str(event[0]))


def delete_event(events):
    if len(events) == 0:
        return events

    print("Which event to delete?")
    for n, event in enumerate(events):
        print(f"{n+1}. {event[0]}")
    print()

    opt = int(input('> '))
    events.pop(opt-1)

    return events

def add_event(events):
    print("Enter event:")
    event = input("> ")

    print("Enter time (HH:MM):")
    time = input("> ")

    # Error handling
    while len(time) != 5:
        print()
        print("Invalid time format! Try again!")
        print("Enter time (HH:MM):")
        time = input("> ")

    hour = time[:2]
    minute = time[-2:]

    events.append((event, hour, minute))
    return sorted(events, key=lambda x: int(x[1] + x[2]))


def mainloop():
    events = []

    while True:
        clear()
        print("== PyPlanner ==")
        print_events(events)

        print()
        print('(A)dd an event')
        print('(D)elete an event')
        print('(E)xit this program')
        print()

        opt = input('> ')

        if opt.lower() == 'a':
            print()
            events = add_event(events)
        elif opt.lower() == 'd':
            print()
            events = delete_event(events)
        elif opt.lower() == 'e':
            exit()
        events = sorted(events, key=lambda x: int(x[1] + x[2]))

if __name__ == '__main__':
    mainloop()
