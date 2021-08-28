import os
import random


class Player:

    def __init__(self, name, token):
        self.name = name
        self.token = token

        # Defaults
        self.money = 1500
        self.position = 0
        self.properties = {'Brown': [], 'Light Blue': [], 'Pink': [], 'Orange': [], 'Red': [], 'Yellow': [], 'Green': [], 'Dark Blue': [], 'Railroad': [], 'Utilities': []}

    def move(self, number, board):
        self.position += number
        self.position %= len(board.board)
        board.board[self.position].occupants.append(self)


class Square:

    PROPERTY_COLORS = {'Brown': 2, 'Light Blue': 3, 'Pink': 3, 'Orange': 3, 'Red': 3, 'Yellow': 3, 'Green': 3, 'Dark Blue': 2, 'Railroad': 4, 'Utilities': 2}

    def __init__(self, name, holder=None, color=None, propertyPrice=None, housePrice=None, rentPrice=None, mortgagePrice=None):

        self.name = name
        self.holder = holder
        self.color = color
        self.occupants = []

        self.propertyPrice = propertyPrice
        self.housePrice = housePrice
        self.rentPrice = rentPrice
        self.mortgagePrice = mortgagePrice

        self.houses = []
        self.hotels = []


class Board:

    def __init__(self):

        self.board = []

        self.board.append(Square(name="Go"))

        self.board.append(Square(name="Mediterranean Avenue", color='Brown', propertyPrice=60, housePrice=50, rentPrice=[2, 10, 30, 90, 160, 250], mortgagePrice=30))

        self.board.append(Square(name="Community Chest"))

        self.board.append(Square(name="Baltic Avenue", color='Brown', propertyPrice=60, housePrice=50, rentPrice=[4, 20, 60, 180, 320, 450], mortgagePrice=30))

        self.board.append(Square(name="Income Tax"))

        self.board.append(Square(name="Reading Railroad", color='Railroad', propertyPrice=200, mortgagePrice=100))

        self.board.append(Square(name="Oriental Avenue", color='Light Blue', propertyPrice=100, housePrice=50, rentPrice=[6, 30, 90, 270, 400, 550], mortgagePrice=50))

        self.board.append(Square(name="Chance"))

        self.board.append(Square(name="Vermont Avenue", color='Light Blue', propertyPrice=100, housePrice=50, rentPrice=[6, 30, 90, 270, 400, 550], mortgagePrice=50))

        self.board.append(Square(name="Connecticut Avenue", color='Light Blue', propertyPrice=120, housePrice=50, rentPrice=[8, 40, 100, 300, 450, 600], mortgagePrice=60))

        self.board.append(Square(name="Jail"))

        self.board.append(Square(name="St. Charles Place", color='Pink', propertyPrice=140, housePrice=100, rentPrice=[10, 50, 150, 450, 625, 750], mortgagePrice=70))

        self.board.append(Square(name="Electric Company", color='Utilities', propertyPrice=150, mortgagePrice=75))

        self.board.append(Square(name="States Avenue", color='Pink', propertyPrice=140, housePrice=100, rentPrice=[10, 50, 150, 450, 625, 750], mortgagePrice=70))

        self.board.append(Square(name="Virginia Avenue", color='Pink', propertyPrice=160, housePrice=100, rentPrice=[12, 60, 180, 500, 700, 900], mortgagePrice=80))

        self.board.append(Square(name="Pennsylvania Railroad", color='Railroad', propertyPrice=200, mortgagePrice=100))

        self.board.append(Square(name="St. James Place", color='Orange', propertyPrice=180, housePrice=100, rentPrice=[14, 70, 200, 550, 750, 950], mortgagePrice=90))

        self.board.append(Square(name="Community Chest"))

        self.board.append(Square(name="Tennessee Avenue", color='Orange', propertyPrice=180, housePrice=100, rentPrice=[14, 70, 200, 550, 750, 950], mortgagePrice=90))

        self.board.append(Square(name="New York Avenue", color='Orange', propertyPrice=200, housePrice=100, rentPrice=[16, 80, 220, 600, 800, 1000], mortgagePrice=100))

        self.board.append(Square(name="Free Parking"))

        self.board.append(Square(name="Kentucky Avenue", color='Red', propertyPrice=220, housePrice=150, rentPrice=[18, 90, 250, 700, 875, 1050], mortgagePrice=110))

        self.board.append(Square(name="Chance"))

        self.board.append(Square(name="Indiana Avenue", color='Red', propertyPrice=220, housePrice=150, rentPrice=[18, 90, 250, 700, 875, 1050], mortgagePrice=110))

        self.board.append(Square(name="Illinois Avenue", color='Red', propertyPrice=240, housePrice=150, rentPrice=[20, 100, 300, 750, 925, 1100], mortgagePrice=120))

        self.board.append(Square(name="B & O. Railroad", color='Railroad', propertyPrice=200, mortgagePrice=100))

        self.board.append(Square(name="Atlantic Avenue", color='Yellow', propertyPrice=260, housePrice=150, rentPrice=[22, 110, 330, 800, 975, 1150], mortgagePrice=130))

        self.board.append(Square(name="Ventnor Avenue", color='Yellow', propertyPrice=260, housePrice=150, rentPrice=[22, 110, 330, 800, 975, 1150], mortgagePrice=130))

        self.board.append(Square(name="Water Works", color='Utilities', propertyPrice=150, mortgagePrice=75))

        self.board.append(Square(name="Marvin Gardens", color='Yellow', propertyPrice=280, housePrice=150, rentPrice=[24, 120, 360, 850, 1025, 1200], mortgagePrice=140))

        self.board.append(Square(name="Go To Jail"))

        self.board.append(Square(name="Pacific Avenue", color='Green', propertyPrice=300, housePrice=200, rentPrice=[26, 130, 390, 900, 1100, 1275], mortgagePrice=150))

        self.board.append(Square(name="North Carolina Avenue", color='Green', propertyPrice=300, housePrice=200, rentPrice=[26, 130, 390, 900, 1100, 1275], mortgagePrice=150))

        self.board.append(Square(name="Community Chest"))

        self.board.append(Square(name="Pennsylvania Avenue", color='Green', propertyPrice=320, housePrice=200, rentPrice=[28, 150, 450, 1000, 1200, 1400], mortgagePrice=160))

        self.board.append(Square(name="Short Line", color='Railroad', propertyPrice=200, mortgagePrice=100))

        self.board.append(Square(name="Chance"))

        self.board.append(Square(name="Park Place", color='Dark Blue', propertyPrice=350, housePrice=200, rentPrice=[35, 175, 500, 1100, 1300, 1500], mortgagePrice=175))

        self.board.append(Square(name="Luxury Tax"))

        self.board.append(Square(name="Boardwalk", color='Dark Blue', propertyPrice=400, housePrice=200, rentPrice=[50, 100, 200, 600, 1400, 1700, 2000], mortgagePrice=200))



class Monopoly:

    def main(self):
        self.setup()
        self.board = Board()
        self.gameloop()

    def setup(self):
        clear = lambda : os.system('clear')
        clear()

        # Make a list of players
        print('\nHow many players? (2-8 players)')
        n = int(input('> '))

        n = min(max(2, n), 8)

        print()

        self.players = []
        tokens = ['☂', '♛', '♆', '♠', '☘', '☠', '☭', '☣', '☂', '☀', '⚛', '☏']

        for i in range(1, n+1):
            print(f'Player {i}')

            print()
            print('Name:')
            name = input('> ')

            print()
            print('Token:')

            for num, token in enumerate(tokens):
                if num < 9:
                    print(' ', end='')
                print(f'{num+1}. {token}')

            while True:
                try:
                    i = int(input('> '))

                    if i == 'exit':
                        return False

                    tokens[i - 1]
                    token = tokens.pop(i - 1)
                    self.players.append(Player(name, token))
                    break

                except:
                    pass

            print()

    def gameloop(self):
        clear = lambda : os.system('clear')

        for player in self.players:
            clear()

            print(f"{player.name}'s Turn ( {player.token} )")
            input('Press Enter to Roll Die')
            print()

            roll = (random.randint(1, 6), random.randint(1, 6))
            print(f"{player.name} rolled {roll[0]} and {roll[1]} ({sum(roll)})")
            player.move(sum(roll), self.board)
            print(f"{player.name} landed on {self.board.board[player.position].name}")
            input()


if __name__ == '__main__':
    game = Monopoly()
    game.main()
