class Pawn:
    def __init__(self, player):
        self.player = player
        self.piece = ('p', 'P')[player - 1]
        
        # For moving two spaces
        self.hasMoved = False
    
    def __str__(self):
        # For displaying the piece
        return self.piece

    def possibleMoves(self, board, start_y, start_x):
        # Returns list of all possible moves

        moves = []

        if self.player == 1:
            
            # Edge of board detection
            if start_y > 0:
                # Moving one space forward
                if board.board[start_y - 1][start_x] == '.':
                    moves.append((start_y - 1, start_x))
                
                # Edge of board detection
                if start_x > 0 :
                    # Capturing Diagonally
                    if board.board[start_y - 1][start_x - 1] != '.':
                        moves.append((start_y - 1, start_x - 1))

                    # En passant
                    if self.hasMoved and board.board[start_y][start_x - 1] != '.':
                        if Pawn.en_passant(start_y, start_x - 1, board):
                            moves.append((start_y - 1, start_x - 1, 'ep'))
                
                # Edge of board detection
                if start_x < 7:
                    # Capturing diagonally the other way
                    if board.board[start_y - 1][start_x + 1] != '.':
                        moves.append((start_y - 1, start_x + 1))

                    # En passant the other way
                    if self.hasMoved and board.board[start_y][start_x + 1] != '.':
                        if Pawn.en_passant(start_y, start_x + 1, board):
                            moves.append((start_y - 1, start_x + 1, 'ep'))

            # If pawn has not moved, it can move two spaces
            if not self.hasMoved:
                # Check if there is a piece in the way
                if board.board[start_y - 1][start_x] == '.' and board.board[start_y - 2][start_x] == '.':
                    moves.append((start_y - 2, start_x))

            return moves

        # If current player is player 2
        else:    
            # Edge of board detection
            if start_y < 7:
                # Moving one space forward
                if board.board[start_y + 1][start_x] == '.':
                    moves.append((start_y + 1, start_x))
                
                # Edge of board detection
                if start_x > 0 :
                    # Capturing Diagonally
                    if board.board[start_y + 1][start_x - 1] != '.':
                        moves.append((start_y + 1, start_x - 1))

                    # En passant
                    if self.hasMoved and board.board[start_y][start_x - 1] != '.':
                        if Pawn.en_passant(start_y, start_x - 1, board):
                            moves.append((start_y + 1, start_x - 1, 'ep'))
                
                # Edge of board detection
                if start_x < 7:
                    # Capturing diagonally the other way
                    if board.board[start_y + 1][start_x + 1] != '.':
                        moves.append((start_y + 1, start_x + 1))

                    # En passant the other way
                    if self.hasMoved and board.board[start_y][start_x + 1] != '.':
                        if Pawn.en_passant(start_y, start_x + 1, board):
                            moves.append((start_y + 1, start_x + 1, 'ep'))

            # If pawn has not moved, it can move two spaces
            if not self.hasMoved:
                # Check if there is a piece in the way
                if board.board[start_y + 1][start_x] == '.' and board.board[start_y + 2][start_x] == '.':
                    moves.append((start_y + 2, start_x))

            return moves
            
    def isValidMove(self, board, start_y, start_x, move_y, move_x):
        # Checks if the move is valid
        # Returns True if move is valid
        # Returns False if move isn't valid

        possibleMoves = self.possibleMoves(board, start_y, start_x)

        if (move_y, move_x) in possibleMoves:
            self.hasMoved = True
            return True
        
        # En Passant handling because En Passant is bizarre
        elif (move_y, move_x, 'ep') in possibleMoves:
            self.hasMoved = True
            if move_x - start_x == 1:
                board.board[start_y][start_x + 1] = '.'
            else:
                board.board[start_y][start_x - 1] = '.'
            return True

        else:
            return False

    @staticmethod
    def en_passant(y, x, board):
        # Method to check if en passant is possible
        # Looks at the previous move made and sees if 
        # a the pawn in question has moved two spaces last move

        piece = board.board[y][x].piece.lower()

        if piece == 'p':
            
            piece_start_y, _, piece_move_y, piece_move_x = board.history[-1]

            if (piece_start_y == 1 or piece_start_y == 6) and abs(piece_start_y - piece_move_y) == 2:
                if x == piece_move_x and y == piece_move_y:
                    return True

        return False
        

class Rook:
    def __init__(self, player):
        self.player = player
        self.piece = ('r', 'R')[player - 1]
        self.hasMoved = False
    
    def __str__(self):
        return self.piece

    def possibleMoves(self, board, start_y, start_x):
        # Returns list of all possible moves

        moves = []
        
        # Moving forward horizontally
        for x in range(start_x + 1, 8):
            moves.append((start_y, x))
            if board.board[start_y][x] != '.':
                break

        # Moving backward horizontally
        for x in range(start_x - 1, -1, -1):
            moves.append((start_y, x))
            if board.board[start_y][x] != '.':
                break

        # Moving forward vertically
        for y in range(start_y + 1, 8):
            moves.append((y, start_x))
            if board.board[y][start_x] != '.':
                break

        # Moving backward vertically
        for y in range(start_y - 1, -1, -1):
            moves.append((y, start_x))
            if board.board[y][start_x] != '.':
                break

        return moves

            
    def isValidMove(self, board, start_y, start_x, move_y, move_x):
        # Checks if the move is valid
        # Returns True if move is valid
        # Returns False if move isn't valid

        possibleMoves = self.possibleMoves(board, start_y, start_x)
        
        if (move_y, move_x) in possibleMoves:
            self.hasMoved = True
            return True
        else:
            return False


class Bishop:
    def __init__(self, player):
        self.player = player
        self.piece = ('b', 'B')[player - 1]
    
    def __str__(self):
        return self.piece

    def possibleMoves(self, board, start_y, start_x):
    # Returns list of all possible moves

        moves = []
        
        # Bishops move diagonally

        # First diagonal
        y = start_y
        x = start_x

        while y < 7 and x < 7:
            y += 1
            x += 1
            moves.append((y, x))
            if board.board[y][x] != '.':
                break

        # Second diagonal
        y = start_y
        x = start_x

        while y > 0 and x > 0:
            y -= 1
            x -= 1
            moves.append((y, x))
            if board.board[y][x] != '.':
                break

        # Third diagonal
        y = start_y
        x = start_x

        while y > 0 and x < 7:
            y -= 1
            x += 1
            moves.append((y, x))
            if board.board[y][x] != '.':
                break

        # Fourth diagonal
        y = start_y
        x = start_x

        while y < 7 and x > 0:
            y += 1
            x -= 1
            moves.append((y, x))
            if board.board[y][x] != '.':
                break

        return moves
    
    def isValidMove(self, board, start_y, start_x, move_y, move_x):
        # Checks if the move is valid
        # Returns True if move is valid
        # Returns False if move isn't valid

        possibleMoves = self.possibleMoves(board, start_y, start_x)

        if (move_y, move_x) in possibleMoves:
            self.hasMoved = True
            return True
        else:
            return False


class Knight:
    def __init__(self, player):
        self.player = player
        self.piece = ('n', 'N')[player - 1]
    
    def __str__(self):
        return self.piece

    def possibleMoves(self, board, start_y, start_x):
        # Returns list of all possible moves

        moves = []

        # Knights move in a L shape 
        # 2 spaces one way and 1 space the other way

        if start_y < 7 and start_x < 6:
            moves.append((start_y + 1, start_x + 2))
        if start_y < 6 and start_x < 7:
            moves.append((start_y + 2, start_x + 1))

        if start_y < 7 and start_x > 1:
            moves.append((start_y + 1, start_x - 2))
        if start_y < 6 and start_x > 0:
            moves.append((start_y + 2, start_x - 1))

        if start_y > 0 and start_x < 6:
            moves.append((start_y - 1, start_x + 2))
        if start_y > 1 and start_x < 7:
            moves.append((start_y - 2, start_x + 1))

        if start_y > 0 and start_x > 1:
            moves.append((start_y - 1, start_x - 2))
        if start_y > 1 and start_x > 0:
            moves.append((start_y - 2, start_x - 1))

        return moves

    def isValidMove(self, board, start_y, start_x, move_y, move_x):
        # Checks if the move is valid
        # Returns True if move is valid
        # Returns False if move isn't valid

        possibleMoves = self.possibleMoves(board, start_y, start_x)

        if (move_y, move_x) in possibleMoves:
            self.hasMoved = True
            return True
        else:
            return False


class Queen:
    def __init__(self, player):
        self.player = player
        self.piece = ('q', 'Q')[player - 1]
    
    def __str__(self):
        return self.piece

    def possibleMoves(self, board, start_y, start_x):
        # Make a temporary bishop and rook object at the starting coordinates
        # Then get possible moves of all of the pieces
        
        moves = []

        # Queen can move diagonally
        temporary_bishop = Bishop(self.player)
        moves.extend(temporary_bishop.possibleMoves(board, start_y, start_x))

        # Queen can move vertically and horizontally
        temporary_rook = Rook(self.player)
        moves.extend(temporary_rook.possibleMoves(board, start_y, start_x))

        return moves

    def isValidMove(self, board, start_y, start_x, move_y, move_x):
        # Checks if the move is valid
        # Returns True if move is valid
        # Returns False if move isn't valid

        possibleMoves = self.possibleMoves(board, start_y, start_x)

        if (move_y, move_x) in possibleMoves:
            self.hasMoved = True
            return True
        else:
            return False

class King:
    def __init__(self, player):
        self.player = player
        self.piece = ('k', 'K')[player - 1]
        self.hasMoved = False
    
    def __str__(self):
        return self.piece

    def possibleMoves(self, board, start_y, start_x):
        # King can move 1 space in any direction       
        moves = []

        if start_y < 7:
            moves.append((start_y + 1, start_x))
            if start_x < 7:
                moves.append((start_y + 1, start_x + 1))
            if start_x > 0:
                moves.append((start_y + 1, start_x - 1))

        if start_y > 0:
            moves.append((start_y - 1, start_x))
            if start_x < 7:
                moves.append((start_y - 1, start_x + 1))
            if start_x > 0:
                moves.append((start_y - 1, start_x - 1))

        if start_x < 7:
            moves.append((start_y, start_x + 1))
        
        if start_x > 0:
            moves.append((start_y, start_x - 1))


        return moves

    def isValidMove(self, board, start_y, start_x, move_y, move_x):
        # Checks if the move is valid
        # Returns True if move is valid
        # Returns False if move isn't valid

        possibleMoves = self.possibleMoves(board, start_y, start_x)

        string = ''
        letters = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h'}
        for move in possibleMoves:
            yy, xx = move
            xx = letters.get(xx + 1)
            string += f'{xx}{8 - yy} '
        print(string)
        input()

        if (move_y, move_x) in possibleMoves:
            self.hasMoved = True
            return True
        else:
            return False

'''
# Tuple to Piece Notation Dictionary
# In order to check if valid moves is correct

string = ''
letters = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h'}
for move in possibleMoves:
    yy, xx = move
    xx = letters.get(xx + 1)
    string += f'{xx}{8 - yy} '
print(string)
input()
'''