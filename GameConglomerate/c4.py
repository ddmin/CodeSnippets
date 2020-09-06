import os


class ConnectFour:

    def __init__(self, horz, vert):
        self.horz = horz
        self.vert = vert
        self.board = [['' for i in range(horz)] for n in range(vert)]


    def display_board(self):
        for i in range(1, self.horz + 1):
            if i < 10:
                print("  " + str(i), end='')
            else:
                print(" " + str(i), end='')
        print()

        for row in self.board:
            for col in row:
                if not col:
                    print("|  ", end='')
                else:
                    print(f"|{col} ", end='')

            print("|")
            print("---" * self.horz + '-')


    def fullAt(self, pos):
        return self.board[0][pos]
   

    def placePiece(self, pos, piece):
        c = self.board[self.vert - 1][pos]
        n = 0 
        while c:
            n += 1
            c = self.board[self.vert - 1 - n][pos]
        
        self.board[self.vert - 1 - n][pos] = piece
        return (self.vert - 1 - n, pos)
           
            
    def vertical(self, last):

        for i in range(self.vert - 3):
            if len(set([self.board[n][last[1]] for n in range(i, i + 4)])) == 1 and self.board[i][last[1]] != '':
                return True

        return False

    def horizontal(self, last):
        
        for i in range(self.horz - 3):
            if len(set([self.board[last[0]][n] for n in range(i, i + 4)])) == 1 and self.board[last[0]][i] != '':
                return True

        return False


    def diagonal(self, last):
        # Forward diagonal
        c = 0
        y = last[0]
        x = last[1]

        while y < self.vert - 1 and x > 0:
            y += 1
            x -= 1

        while self.board[y][x] != self.board[last[0]][last[1]]:
            y -= 1
            x += 1 

        try:
            while self.board[y][x] == self.board[last[0]][last[1]]:
                c += 1
                y -= 1
                x += 1
                if c == 4:
                    return True
        except:
            pass

        # Reverse diagonal
        c = 0
        y = last[0]
        x = last[1]

        while y < self.vert - 1 and x < self.horz - 1:
            y += 1
            x += 1

        while self.board[y][x] != self.board[last[0]][last[1]]:
            y -= 1
            x -= 1

        try:
            while self.board[y][x] == self.board[last[0]][last[1]]:
                c += 1
                y -= 1
                x -= 1
                if c == 4:
                    return True

        except:
            pass

        return False


    def gameloop(self):

        clear = lambda : os.system('clear')

        pieces = ['O', 'X']
        turn = 0

        while True:
            clear()
            self.display_board()

            print(f"{pieces[turn]}'s turn")
            print("Move?")
            
            try:
                move = input("> ")
                if move == "exit":
                    return False
                move = int(move) - 1
            except:
                move = -1
            
            if move > -1 and move < self.horz and not self.fullAt(move):
                last = self.placePiece(move, pieces[turn])

                if self.vertical(last) or self.horizontal(last) or self.diagonal(last):
                    clear()
                    self.display_board()
                    print(f"{pieces[turn]} wins!")
                    return False

                turn = not turn
            
if __name__ == '__main__':
    # Initialize board size here
    game = ConnectFour(horz=7, vert=6)
    game.gameloop()
