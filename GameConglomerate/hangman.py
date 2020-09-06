import os

class Hangman:
    def __init__(self, phrase):
        self.phrase = phrase
        self.guesses = 8
        self.guessed_letters = []

    def show_blanks(self):
        for letter in self.phrase:
            if not letter.isalpha():
                print(letter, end=' ')

            elif letter.lower() not in self.guessed_letters:
                print('_', end=' ')

            else:
                print(letter, end=' ') 
        print('\n')


    def check_win(self):
        for letter in self.phrase:
            if letter.isalpha() and letter.lower() not in self.guessed_letters:
                return False
        return True


    def gameloop(self):
       clear = lambda : os.system('clear')
       while True:
          clear()

          self.show_blanks()

          print(f'Guesses left: {self.guesses}')

          if self.check_win():
              print("You Win!")
              break

          print('Guess a letter:')

          while True:
              guess = input('> ')
              if guess.isalpha() and len(guess) == 1:
                  if guess not in self.guessed_letters:
                      break
                  else:
                      print("You've already guessed that letter.")
              else:
                  print("That's not a letter.")

          if guess not in self.phrase.lower():
              self.guesses -= 1
              if self.guesses == 0:
                  clear()
                  print("You Lose.")
                  print(f'"The phrase was: {self.phrase}"')
                  return False

          self.guessed_letters.append(guess)


if __name__ == '__main__':
    # Change phrase to guess here.
    game = Hangman('Hangman is a fun game to play. Neat-o!')
    game.gameloop()
