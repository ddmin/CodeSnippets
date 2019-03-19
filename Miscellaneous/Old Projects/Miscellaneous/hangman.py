def gameloop():
    lives = 5
    
    letters_guessed = []
    letters_correct = []

    word = input('Enter a word: ')
    WIN = len(set([x.lower() for x in word if x.isalpha()]))

    display_board(word = word, correct = letters_correct)

    while lives != 0 and len(letters_correct) != WIN:

        guess = ''

        while not(len(guess) == 1 and guess.isalpha()):
            guess = input('Guess a letter: ').lower()

        if guess not in letters_guessed:
            letters_guessed.append(guess)

            if guess in word.lower():
                letters_correct.append(guess)
            
            else:
                lives -= 1
                print(f'"{guess}" is not in the word.')
                print(f'Lives: {lives}')
                
            display_board(word = word, correct = letters_correct)

        else:
            print(f'You have already guessed "{guess}".')
    
    if lives == 0:
        print()
        print("You lose...")
        print(f'The word was: {word}')
    else:
        print()
        print("You win!")
        print(f'Lives left: {lives}')

def display_board(word, correct):
    print(' '.join([word[x] if word[x].lower() in correct or not(word[x].isalpha()) else '_' for x in range(len(word))]))

if __name__ == '__main__':
    gameloop()