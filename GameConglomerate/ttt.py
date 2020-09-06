import os

class TicTacToe:
    
    def __init__(self, gamesize):
        self.gamesize = gamesize
        self.board = board = [['' for i in range(self.gamesize)] for n in range(self.gamesize)]

    def display_board(self):
        n = 1 

        print("-" + "-----" * self.gamesize)

        for row in self.board:
            print("| ", end='')
            for col in row:
                if not col:
                    if n >= 100:
                        print(n, end='| ')
                    elif n >= 10:
                        print(n, end=' | ')
                    else:
                        print(n, end='  | ')
                else:
                    print(col, end='  | ')
                n += 1 

            print("\b")
            print("-" + "-----" * self.gamesize) 
        print()


    def vertical(self):
        for col in range(self.gamesize):
            if len(set([self.board[i][col] for i in range(self.gamesize)])) == 1 and self.board[0][col] != "":
                return True
        return False


    def horizontal(self):
        for row in self.board:
            if len(set(row)) == 1 and row[0] != "":
                return True
        return False


    def diagonal(self):
        if len(set([self.board[i][i] for i in range(self.gamesize)])) == 1 and self.board[0][0] != "":
            return True
        
        if len(set([self.board[i][self.gamesize-1-i] for i in range(self.gamesize)])) == 1 and self.board[0][self.gamesize-1] != "":
            return True
        return False


    def checkWin(self):
        if self.vertical() or self.horizontal() or self.diagonal():
            return True

    def gameloop(self):
        clear = lambda : os.system("clear")

        marks = ["x", "o"]
        turn = 0 

        while True:
            clear()
            self.display_board()  

            move = -1 
            while True: 
                print(marks[turn%2] + "'s turn")
                print(f"Move? (1-{self.gamesize ** 2})")

                try:
                    move = input("> ")
                    if move == 'exit':
                        return False
                    move = int(move) - 1

                except:
                    move = -1

                if move > -1 and move < (self.gamesize ** 2): 
                    if not self.board[move // self.gamesize][move % self.gamesize]:
                        self.board[move // self.gamesize][move % self.gamesize] = marks[turn%2]

                        if self.checkWin():
                            clear()
                            self.display_board()
                            print("Player " + marks[turn%2] + " wins!")
                            return False

                        if turn == self.gamesize ** 2 - 1:
                            clear()
                            self.display_board()
                            print("Tie!")
                            return False


                        turn += 1
                        break

if __name__ == '__main__':
    # Initialize board size here 
    game = TicTacToe(5)
    game.gameloop()
