class Player:

    # combat stats
    stats = {
                "Attack": 1,
                "Defense": 1,
                "Speed": 1,
                "Crit Rate": 0,
                "Crit DMG": 0,
            }

    def __init__(self, name="Gil"):
        self.name = name

    def __str__(self):
        string = f"{self.name}"
        stats = ''
        return string

    def stat_screen(self, points=0):
        for stat, val in self.stats.items():
            print(stat, val)

def main():
    player = Player()
    print(player)
    player.stat_screen()

if __name__ == '__main__':
    main()
