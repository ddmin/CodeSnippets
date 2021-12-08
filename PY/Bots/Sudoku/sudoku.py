import csv
import random
import time

# Pretty Print the board
def print_board(board):
    for i in range(len(board)):
        if i != 0 and i % 3 == 0:
            print("----------------------")
        for n in range(len(board[i])):
            print(board[i][n], end=' ')
            if (n+1) != 9 and (n+1) % 3 == 0:
                print('|', end=' ')
        print()

# Return a tuple of the position of the first blank
def find_blank(board):
    for col in range(len(board)):
        for row in range(len(board[col])):
            if board[col][row] == 0:
                return (col, row)
    return None

# Check if the number in the position is valid
def is_valid(board, num, pos):
    col, row = pos

    # Check row
    for n in range(len(board[col])):
        if num == board[col][n] and n != row:
            return False

    # Check column
    for n in range(9):
        if num == board[n][row] and n != col:
            return False

    # Check square
    x = row // 3
    y = col // 3
    for yy in range(y * 3, y * 3 + 3):
        for xx in range(x * 3, x * 3 + 3):
            if board[yy][xx] == num and yy != col and xx != row:
                return False

    return True

# Solve the board state
def solve(board):
    blank = find_blank(board)
    if not blank:
        return True
    col, row = blank

    for n in range(1, 10):
        if is_valid(board, n, (col, row)):
            board[col][row] = n
            if solve(board):
                return True
        board[col][row] = 0

    return False

# Converts string format to list format
def convert(string):
    return [[int(string[n]) for n in range(x*9, x*9+9)] for x in range(9)]

# Fetches a puzzle from the csv
def fetch_puzzle():
    n = random.randint(1, 1000000)
    with open('puzzles.csv') as file:
        r = csv.reader(file, delimiter=',')
        count = 0
        for row in r:
            if count == n:
                return (count, row)
            count += 1

# Solve a random puzzle
def main():
    num, lst = fetch_puzzle()
    puzzle, solution = lst

    puzzle = convert(puzzle)
    solution = convert(solution)

    print(f'Puzzle #{num}\n')
    print('Original State')
    print_board(puzzle)

    start = time.time()
    solve(puzzle)
    end = time.time()
    elapsed = round((end - start), 5)

    if puzzle == solution:
        print('\nSolved State')
        print_board(puzzle)
        print(f'\n(Solved in {elapsed} seconds)')

    # This should theoretically never run
    else:
        print('Incorrect solution!')

if __name__ == '__main__':
    main()
