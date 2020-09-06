import os
from board import Board

# Check operating system and create a method to clear terminal screen 
if os.name == 'posix':
    clear = lambda: os.system('clear')
else:
    clear = lambda: os.system('cls')

if not os.path.isdir("Game Files"):
    os.mkdir("Game Files")

with open("Game Files\\chess_game.txt", "w") as f:
    f.write("")

def gameloop():
    # Create Board object
    board = Board()

    # Player 1 goes first
    player_turn = 1

    while True:
        # Clear screen every turn
        clear()

        # Display current player's turn
        print("   ", end = '')

        if player_turn == 1:
            print(f"player {player_turn}'s turn\n")
        else:
            print("                       ", end = '')
            print(f"PLAYER {player_turn}'S TURN\n")
        
        board.print_board(player_turn)

        # Get user input for piece
        print("Coordinates of piece to move?")
        piece = input("> ").upper()

        # Get user input for destination
        print("Coordinate of position to move to?")
        move_to = input("> ").upper()

        # Check if input is 2 characters long
        if len(piece) != 2 or len(move_to) != 2:
            print("Not a valid move.")
            input()
            continue

        # Check if first character is a letter
        if not piece[0].isalpha() or not move_to[0].isalpha():
            print("Not a valid move.")
            input()
            continue

        # Check if first character is a digit
        if not piece[1].isdigit() or not move_to[1].isdigit():
            print("Not a valid move.")
            input()
            continue

        # Coordinate of the starting position
        piece_tuple = (piece[0], int(piece[1]))

        # Coordinate of destination
        move_tuple = (move_to[0], int(move_to[1]))

        # Check if move was valid
        # If move is valid make the move
        if not board.move(piece_tuple, move_tuple, player_turn):
            print("Not a valid move.")
            input()
            continue
        
        # Change the player's turn
        player_turn = abs(player_turn - 3)
        
        board.record_move()

if __name__ == '__main__':
    gameloop()