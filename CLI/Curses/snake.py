import curses
from curses import textpad


def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(True)
    stdscr.timeout(50)

    sh, sw = stdscr.getmaxyx()
    box = [[3, 3], [sh-3, sw-3]]
    textpad.rectangle(stdscr, box[0][0], box[0][1], box[1][0], box[1][1])

    snake = [[sh//2, sw//2-1], [sh//2, sw//2], [sh//2, sw//2+1]]
    direction = 108

    for y, x in snake:
        stdscr.addstr(y, x, '#')

    while True:
        key = stdscr.getch()

        if key in [104, 106, 107, 108]:
            direction = key

        head = snake[0]

        if direction == 108:
            new_head = [head[0], head[1]+1]
        elif direction == 104:
            new_head = [head[0], head[1]-1]
        elif direction == 107:
            new_head = [head[0]-1, head[1]]
        elif direction == 106:
            new_head = [head[0]+1, head[1]]

        snake.insert(0, new_head)
        stdscr.addstr(new_head[0], new_head[1], '#')

        stdscr.addstr(snake[-1][0], snake[-1][1], ' ')
        snake.pop()

        if (snake[0][0] in (box[0][0], box[1][0]) or snake[0][1] in (box[0][1], box[1][1]) or snake[0] in snake[1:]):

            msg = "Game Over!"
            stdscr.addstr(sh//2, sw//2-len(msg)//2, msg)
            stdscr.nodelay(False)
            stdscr.getch()


curses.wrapper(main)
