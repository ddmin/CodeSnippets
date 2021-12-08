# [Hard] Challenge 5

import random
import sys
import os

clear = lambda : os.system('clear')

class Pirate:
    def __init__(self, name, health, speed, attacks):
        self.name = name

        self.health = health
        self.speed = speed

        # Attacks - {'Attack Name': [ATK Damage, Accuracy (1/n)]}
        self.attacks = attacks

def main():
    # Character Roster
    luffy = Pirate('Luffy D. Monkey', 150, 150, {'Gomu Gomu no Pistol': [20, 1],
                                               'Gomu Gomu no Bazooka': [50, 2]})

    zoro = Pirate('Roronoa Zoro', 180, 100, {'San-To-Ryu': [65, 3],
                                             'Oni Giri': [100, 8]})

    sanji = Pirate('Sanji', 150, 200, {'Epaule': [40, 1],
                                       'Poitrine': [80, 5]})

    usopp = Pirate('Usopp', 100, 120, {'Tabasco Boshi': [50, 1],
                                        'Usopp Hammer': [80, 2]})

    nami = Pirate('Nami', 130, 100, {'Clima-tact': [20, 1],
                                     'Thunder Ball': [60, 2]})

    chopper = Pirate('Tony Tony Chopper', 150, 150, {'Horn Point': [20, 1],
                                                     'Brain Point': [300, 15]})

    robin = Pirate('Nico Robin', 120, 150, {'Dos Fleur': [30, 1],
                                            'Treinta Fleur': [60, 2]})

    # Enemies
    arlong = Pirate('Arlong', 300, 140, {'Dive': [20, 2],
                                         'Spiked Nose': [40, 3],
                                         'Shark on Darts': [100, 8]})

    crocodile = Pirate('Crocodile', 300, 120, {'Sand Blast': [15, 1],
                                              'Dessicate': [45, 2],
                                              'Poison Hook': [80, 10]})

    enel = Pirate('God Enel', 200, 3000, {'Kaminari': [10, 2],
                                           'El-Thor': [20, 2],
                                           'Mantra': [50, 1]})

    pirates = [luffy, zoro, sanji, usopp, nami, chopper, robin]
    enemies = [crocodile, enel]

    # enemy = random.choice(enemies)
    enemy = arlong

    clear()
    print("== Mugiwara Py-rates ==")
    print()
    print(f'> {enemy.name} has challenged you!')
    print()
    print("Choose your ch-arrr-acter!")

    for n, pirate in enumerate(pirates):
        print(f'  {n+1}. {pirate.name}')

    print()

    n = input('>> ')
    if n == 'exit':
        return 0

    player = pirates[int(n) - 1]

    clear()

    if player.speed > enemy.speed:
        combatants = [player, enemy]
    elif enemy.speed > player.speed:
        combatants = [enemy, player]
    else:
        combatants = random.choice([[player,enemy], [enemy, player]])

    turn = 0
    while player.health > 0 and enemy.health > 0:
        clear()

        print(f'== {combatants[0].name} v.s. {combatants[1].name} ==')
        print()
        print(f'{combatants[0].name} - {combatants[0].health} HP')
        print(f'{combatants[1].name} - {combatants[1].health} HP')
        print()
        print(f"{combatants[turn].name}'s Turn")

        for n, attack in enumerate(combatants[turn].attacks):
            power = combatants[turn].attacks[attack][0]
            acc = int(1 / combatants[turn].attacks[attack][1] * 100)
            print(f'  {n+1}. {attack} (POW - {power} | ACC - {acc}%)')

        try:
            if combatants[turn] == player:
                i = input('>> ')
                if i == 'exit':
                    break
            else:
                i = random.randint(1, len(combatants[turn].attacks))

            c = int(i) - 1
            atk = list(combatants[turn].attacks)[c]
            stat = combatants[turn].attacks[atk]

        except:
            print()
            print('Enter a valid number!')
            print()
            continue

        print()
        print(f'> {combatants[turn].name} used {atk}.')
        if random.randint(1, stat[1]) == 1:
            print(f'> It did {stat[0]} damage.')
            combatants[not turn].health -= stat[0]
        else:
            print(f'> {combatants[turn].name} missed!')

        print()
        turn = not turn
        input('Any key to continue...')

    turn = not turn
    clear()
    print(f'{combatants[0].name} - {combatants[0].health} HP')
    print(f'{combatants[1].name} - {combatants[1].health} HP')
    print()
    if combatants[0].health <= 0 or combatants[1].health <= 0:
        print(f'{combatants[turn].name} wins!')

if __name__ == '__main__':
    main()
