import curses
import time

menu = ['Home', 'Play', 'Scoreboard', 'About Us', 'Exit']


def displayMenu(stdscr, selected):
    h, w = stdscr.getmaxyx()
    stdscr.clear()
    for i, row in enumerate(menu):
        x = w//2 - len(row)//2
        y = h//2 - len(menu)//2 + i
        if i == selected:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, x, row)
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(y, x, row)

    stdscr.refresh()


def main(stdscr):
    h, w = stdscr.getmaxyx()
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

    selected = 0
    displayMenu(stdscr, selected)

    key = 0
    while True:
        key = stdscr.getch()
        stdscr.clear()

        if key == 107:
            selected -= 1
        elif key == 106:
            selected += 1
        elif key == 108:
            if menu[selected] == 'Exit':
                break
            stdscr.clear()
            text = f"You pressed '{menu[selected]}'"
            x = w // 2 - len(text)//2
            y = h // 2
            stdscr.addstr(y, x, text)
            stdscr.refresh()
            stdscr.getch()

        elif key in [113, 27]:
            break

        selected = selected % len(menu)
        displayMenu(stdscr, selected)


curses.wrapper(main)
