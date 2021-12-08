# [Hard] Challenge 2


import time


class Stopwatch:

    def __init__(self):

        self.start_time = 0

        self.total_time = 0
        self.laps = []

        self.start = False

    def toggle(self):
        self.start_time = time.time()
        self.start = not self.start

        print()
        if self.start:
            print("Stopwatch has started.")
        else:
            print("Stopwatch has stopped.")

    def lap(self):
        self.laps.append(format_time(self.total_time))
        print()
        print(f"Lap {len(self.laps)}: {format_time(self.total_time)}")

    def reset(self):
        self.total_time = 0
        self.start = False
        self.laps = []

        print()
        print("Stopwatch was reset.")

    def current_time(self):
        print()
        print(f'Time: {format_time(self.total_time)}')

    def update(self):
        if self.start:
            self.total_time += (time.time() - self.start_time)
        self.start_time = time.time()

    def display_laps(self):
        print()
        if not self.laps:
            print("No laps.")
            return False
        for n, i in enumerate(self.laps):
            print(f'Lap {n+1}: {i}')

def format_time(t):

    milli = str(t - int(t))[2:4]
    minute = int(t) // 60
    second = int(t) - (60 * minute)

    return f'{minute}:{str(second).zfill(2)}:{str(milli).zfill(2)}'


def main():
    watch = Stopwatch()
    while True:
        print()
        print("(S)tart / (S)top | (L)ap | (R)eset | Display (C)urrent Time | (D)isplay Laps")

        if watch.start:
            print("Stopwatch is running...")
        else:
            print("Stopwatch is stopped.")

        opt = input("> ")
        watch.update()

        if opt.lower() == 's':
            watch.toggle()

        elif opt.lower() == 'l':
            watch.lap()

        elif opt.lower() == 'r':
            watch.reset()

        elif opt.lower() == 'c':
            watch.current_time()

        elif opt.lower() == 'd':
            watch.display_laps()

        elif opt.lower() == 'q':
            exit()

        else:
            print("Not a valid option.")

if __name__ == '__main__':
    main()
