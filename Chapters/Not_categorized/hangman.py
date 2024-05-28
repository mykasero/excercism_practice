# Game status categories
# Change the values as you see fit
STATUS_WIN = 'win'
STATUS_LOSE = 'lose'
STATUS_ONGOING = 'ongoing'


class Hangman:
    def __init__(self, word):
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING
        self.word = word
        self.masked_word = "_" * len(self.word)
        self.found_char = False
        self.already_found = []
        self.status = None

    def guess(self, char):
        if self.remaining_guesses < 0 or self.status == STATUS_WIN:
            raise ValueError("The game has already ended.")
        else:
            self.found_char = False

            for i in range(len(self.word)):
                if char == self.word[i] and char not in self.already_found:
                    self.masked_word = self.masked_word[:i] + char + self.masked_word[i+1:len(self.masked_word)]
                    self.found_char = True

            if not self.found_char:
                self.remaining_guesses -= 1
            elif self.found_char:
                self.already_found.append(char)
    def get_masked_word(self):
        return self.masked_word

    def get_status(self):
        if "_" not in self.masked_word:
            self.status = STATUS_WIN
        elif self.remaining_guesses > 0 and "_" in self.masked_word:
            self.status = STATUS_ONGOING
        else:
            self.status = STATUS_LOSE

        return self.status
'''
Instructions
Implement the logic of the hangman game using functional reactive programming.

Hangman is a simple word guessing game.

Functional Reactive Programming is a way to write interactive programs. 
It differs from the usual perspective in that instead of saying "when the button is pressed increment the counter", 
you write "the value of the counter is the sum of the number of times the button is pressed."

Implement the basic logic behind hangman using functional reactive programming. 
You'll need to install an FRP library for this, this will be described in the language/track specific files of the exercise.

!!!
Python Special Instructions
A third party library is not required for this exercise. Please ignore the instructions regarding FRP library.
'''
# link to test cases not available
