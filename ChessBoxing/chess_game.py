import chess
import os

'''
Chess Boxing: Brains vs Brawn
'''

clear = lambda : os.system('cls' if os.name == 'nt' else 'clear')

def print_board(board):
    for letter in ('  a b c d e f g h'):
        print(letter, end='')

    print()

    rows = [str(8-r) + ' ' + board.__str__()[r*16: r*16+15] for r in range(8)]

    for row in rows:
        print(row)


board = chess.Board()

turn = 0
current_player = 'White'
while True:
    clear()
    print(f"{current_player}'s Turn\n")
    print_board(board)
    move = input(">> ")
    
    try:
        board.push_san(move)
        turn = not turn
        if board.is_checkmate():
            break
        current_player = ('White', 'Black')[turn]

    except:
        print("Invalid move.")
        input()

print(f'{current_player} mate!')

'''
TODO:
- Handle Checks
- Handle castling
'''