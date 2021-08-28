from pieces import *

import os

class Board:

    def __init__(self):
        # Create an empty 8x8 board
        board = [['.' for x in range(8)] for y in range(8)]

        # Fill in the major pieces
        for i, piece in enumerate([Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]):
            board[0][i] = piece(2)
            board[7][i] = piece(1)

        # Fill in the pawns
        for i in range(8):
            board[1][i] = Pawn(2)
            board[6][i] = Pawn(1)

        self.board = board

        self.history = []


    def print_board(self, turn):

        letters = 'ABCDEFGH'
        antiletters = 'HGFEDCBA'

        board = self.board
        antiboard = [row[::-1] for row in self.board][::-1]

        # Print the letters
        print('   ', end='')
        for letter in letters:
            print(letter, end=' ')
       
        print('       ', end='')
        for letter in antiletters:
            print(letter, end=' ')
        print('\n')

        # Print the numbers and the rows
        for i, column_zip in enumerate(zip(board, antiboard)):
            column, anticolumn = column_zip

            # Numbers are descending for player 1
            number = 8 - i

            # Numbers are ascending for player 2
            antinumber = i + 1

            print(number, end = '  ')
            for n, square in enumerate(column):
                if square != '.':
                    # print(square, end = ' ')
                    print(square, end = ' ')
                else:
                    if i % 2 == 0:
                        print((' ', '.')[n % 2 != 0], end = ' ')
                    else:
                        print((' ', '.')[n % 2 == 0], end = ' ')

            print('    ' + str(antinumber), end = '  ')

            for n, square in enumerate(anticolumn):
                if square != '.':
                    print(square, end = ' ')
                else:
                    if i % 2 == 0:
                        print((' ', '.')[n % 2 != 0], end = ' ')
                    else:
                        print((' ', '.')[n % 2 == 0], end = ' ')

            print()

        print()

    def record_move(self):
        # Take all of the moves and save it in a txt file
        
        letters = {1: 'a', 2: 'b', 3: 'c', 4: 'd',
                   5: 'e', 6: 'f', 7: 'g', 8: 'h'}

        game = ''

        for move_number, move in enumerate(self.history):
            start_y, start_x, move_y, move_x = move

            start_x = letters.get(start_x + 1) 
            move_x = letters.get(move_x + 1)

            start_y = 8 - start_y
            move_y = 8 - move_y

            game += f'{move_number + 1}. {start_x}{start_y} to {move_x}{move_y}\n'

        save_file = os.path.join(os.path.join(os.getcwd(), "Game Files"), "chess_game.txt")

        with open(save_file, 'w') as f:
            f.write(game)

    def move(self, start_coordinates, move_coordinates, turn):
        # Moves a piece on the board from the starting coordinate to the destination coordinate
        # Returns True if the move was made
        # Returns False if the move is invalid

        start_x, start_y = start_coordinates
        move_x, move_y = move_coordinates

        letters = {'A': 1, 'B': 2, 'C': 3, 'D': 4,
                   'E': 5, 'F': 6, 'G': 7, 'H': 8}
        
        # Convert letters into numbers
        start_x = letters.get(start_x)
        move_x = letters.get(move_x)

        # Check if the letter input is valid
        if start_x is None or move_x is None:
            return False

        # Check if the number input is valid
        for position in (start_x, move_x, start_y, move_y):
            if position < 1 or position > 8:
                return False 

        # Check if the input is the same coordinate
        if start_y == move_y and start_x == move_x:
            return False
        
        # Y coordinates are backwards
        start_y = 8 - start_y
        move_y = 8 - move_y

        # X coordinates are greater by 1
        start_x = start_x - 1
        move_x = move_x - 1

        piece = self.board[start_y][start_x]

        # Check if the position on the board is empty
        if piece == '.':
            return False

        # Check if player is moving their own piece
        if self.board[start_y][start_x].player != turn:
            return False

        # Check if player is trying to capture their own piece
        if self.board[move_y][move_x] != '.':
            if self.board[move_y][move_x].player == turn:
                return False

        # Check if the piece is able to make that move
        if not piece.isValidMove(self, start_y, start_x, move_y, move_x):
            return False

        # Record the move in the history
        self.history.append((start_y, start_x, move_y, move_x))

        # Move the piece from the starting location to the destination
        self.board[move_y][move_x] = self.board[start_y][start_x]

        # Replace the original location with an empty space
        self.board[start_y][start_x] = '.'

        # If the move was made successfully return True
        return True