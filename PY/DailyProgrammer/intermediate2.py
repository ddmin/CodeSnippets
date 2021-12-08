# [Intermediate] Challenge 2


# Pretty Print user input
def prinput(msg):
    print()
    print(msg)
    return input("> ")

# Shorthand way of validating user input
def validate(choice, lst, msg):
    while choice.lower() not in lst:
        print()
        print("That's not a valid option.")
        choice = prinput(msg)
    return choice


# Main gameloop
def main():
    print("== Pythons and Puzzles ==")
    print("A Text Based Adventure Game")

    name = prinput("Enter you name, hero:")

    print()
    print(f'Welcome, ' + name + '!')
    print()

    # First Choice
    print('You encounter 3 doors. Which do you enter?')
    print('1. (L)eft')
    print('2. (M)iddle')
    print('3. (R)ight')

    choice1 = prinput("Which door?")
    choice1 = validate(choice1, ['l', 'm', 'r'], "Which door?")

    if choice1.lower() == 'l':
        print()
        print("From the ceiling drops a mace. It impales you.")
        print("You die an instant death.")
        print("== GAME OVER ==")
        exit()
    elif choice1.lower() == 'm':
        print()
        print("A horde of pythons attack you!")
        print()
        print("What do you do?")
        print("1. (A)ttack with a sword")
        print("2. (S)hoot them with a bow")
        print("3. (F)lee the scene")

        choice2 = prinput("Which action?")
        choice2 = validate(choice2, ['a', 's', 'f'], "Which action?")

        if choice2.lower() == 'a':
            print()
            print("You jab a sword at one of the pythons, but they parry.")
            print("The other pythons grab your sword and break it in half.")
            print("== GAME OVER ==")
            exit()
        elif choice2.lower() == 's':
            print()
            print("You shoot one of the pythons in the eye.")
            print("You reach in your quiver for another, but you have no more.")
            print("== GAME OVER ==")
            exit()
        elif choice2.lower() == 'f':
            print()
            print("You run as fast as you can, but the pythons are faster.")
            print("One grabs your legs, and you fall to the ground.")
            print("== GAME OVER ==")
            exit()

    elif choice1.lower() == 'r':
        print()
        print("A horde of gnomes attack you!")
        print("You try to resist, but their power is overwhelming.")
        print("== GAME OVER ==")
        exit()

if __name__ == '__main__':
    main()
