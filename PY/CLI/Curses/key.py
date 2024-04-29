import curses


def main(stdscr):
    stdscr.keypad(False)

    stdscr.clear()

    while True:
        key = stdscr.getch()
        stdscr.clear()
        stdscr.addstr(0, 0, str(key))
        stdscr.refresh()


curses.wrapper(main)
