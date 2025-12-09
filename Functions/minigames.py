from Functions.misc import print_text
from Assets.text import wordle_info


def wordle(word: str) -> bool:
    green = '\033[32m'
    yellow = '\033[33m'
    reset = '\033[0m'

    print_text(wordle_info, 0.025)
    word = list(word)
    guesses = 0
    while guesses < 6:
        print(f"attempt {guesses + 1}")
        guess = input("Guess the word: ")
        if len(guess) == 5:
            guess = list(guess.lower())
            i = 0
            correct_letters = 0
            checked_guess = ''
            while i < 5:
                if guess[i] == word[i]:
                    guess[i] = green + guess[i] + reset
                    correct_letters += 1
                elif guess[i] in word:
                    guess[i] = yellow + guess[i] + reset
                checked_guess += guess[i]
                i += 1
            print(checked_guess)
            if correct_letters == 5:
                return True
            guesses += 1
        else:
            print_text("Only guess a word using 5 letters!\n", 0.075)
    return False