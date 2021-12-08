# [Hard] Challenge 6

import random


# return (row, num)
def make_move(board):
    for n, i in enumerate(board):
        if i != 0:
            return (n, random.randint(1, i))

# print board
def print_board(board):
    m = max(board)
    for n, i in enumerate(board):
        print(str(n+1) + '. ' + ('o' * i).ljust(m+3) + '(' + str(i) + ')')
    print()

# run game
def gameloop():
    turn = 0
    players = ['player', 'bot']
    board = [1, 3, 5, 7]

    while board != [0, 0, 0, 0]:

        print(f'{players[turn].upper()}\'s turn')

        # print board
        print_board(board)

        # Player Move
        if players[turn] == 'player':
            print('Row:')
            row = int(input('> ')) - 1

            print('How many to remove?:')
            num = int(input('> '))

            print()

            if num > board[row]:
                print('You cannot perform that action.')
                print()
                continue

            board[row] -= num

        # Bot Move
        else:
            row, num = make_move(board)
            board[row] -= num

            print(f'BOT removed {num} from row {row + 1}')
            print()

        turn = not turn

    print(f'{players[not turn].upper()} takes the last piece')
    print(f'{players[turn].upper()} wins')

def main():
    gameloop()

if __name__ == '__main__':
    main()
