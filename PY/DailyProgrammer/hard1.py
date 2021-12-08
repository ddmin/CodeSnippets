# [Hard] Challenge 1

import random


n = random.randint(1, 100)

lo_guess = 1
hi_guess = 100

guess = 50
lives = 10

print("Choosing a number between 1 - 100...")
print("The number is: " + str(n))
print()

while guess != n:
    print("Remaining Lives: " + str(lives))

    lives -= 1
    if lives == -1:
        print()
        print(f"GAME OVER! The COMPUTER was unable to guess the number! ({n})")
        exit()

    print("COMPUTER's Guess: " + str(guess))
    print()
    print("(H)igher or (L)ower?:")
    prompt = input("> ")

    while prompt.lower() not in ['h', 'l']:
        print()
        print("Not a valid response. Enter either H or L.")

        print("Is the number (H)igher or (L)ower?:")
        prompt = input("> ")

    print()
    if prompt.lower() == 'h':
        lo_guess = guess
        guess = (guess + hi_guess) // 2

    elif prompt.lower() == 'l':
        hi_guess = guess
        guess = (guess + lo_guess) // 2

print("COMPUTER's Guess: " + str(guess))
print("The COMPUTER guessed correctly!")
