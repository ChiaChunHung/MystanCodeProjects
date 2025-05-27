"""
File: hangman_game.py
Name: Chia-Chun, Hung
--------------------------------------------------
This program simulates the classic Hangman game.

The game selects a random word from a fixed list. The user is
prompted to guess one letter at a time. Correct guesses reveal
the corresponding letters in the word, while incorrect guesses
reduce the number of remaining attempts. The player wins if they
successfully guess the full word before exhausting all attempts.

The program reinforces string manipulation, control flow,
loop design, and input validation.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    Runs the Hangman game using a randomly selected word.
    """
    answer = random_word()                                                  # Obtain a random word as the answer
    first_word_look = first_look_of_word(answer)                            # Create the initial dashed word
    process(first_word_look, answer, N_TURNS)                               # Start the game process


def first_look_of_word(answer):
    """
    Creates the initial dashed word (e.g., '------') based on the length of the answer.
    :param answer: str, the correct answer to be guessed
    :return: str, a string of dashes representing unrevealed letters
    """
    word_look = ''
    for i in range(len(answer)):                                            # For each letter in the answer,
        word_look += '-'                                                    # add a dash to represent unrevealed letters
    return word_look


def process(first_word_look, answer, n_turns):
    """
    :param first_word_look: str, the current state showing guessed letters and dashes
    :param answer: str, the answer word to guess
    :param n_turns: int, number of wrong guesses remaining
    """
    while True:
        # maintain game loop. Continues until player either wins or runs out of guesses.
        if n_turns != 0:                                                    # player still has guesses left
            if first_word_look != answer:
                print('The word looks like: ' + first_word_look)            # show the current state of the word
                print('You have ' + str(n_turns) + ' wrong guesses left')   # show the remaining guesses
                while True:
                    guess = input('Your guess: ')                           # prompt user for input until valid guess is entered
                    if guess.isalpha():                                     # Validate input
                        guess = guess.upper()                               # Convert to uppercase for case-insensitive comparison
                        if len(guess) == 1:
                            if guess in answer:
                                ans = ''
                                for i in range(len(answer)):
                                    if answer[i] == guess:                  # letter was guessed correctly
                                        ans += guess                        # update the visible word accordingly
                                    else:
                                        ans += first_word_look[i]
                                first_word_look = ans
                                print('You are correct!')
                                break                                       # end current guess loop, continue main loop
                            else:                                           # Letter was incorrect, reduce the number of remaining guesses
                                print('There is no ' + guess + ' in the word.')
                                n_turns -= 1
                                break
                        else:                                               # input is multiple letters, invalid
                            print('Illegal format.')
                    else:
                        print('Illegal format.')                            # Input is not a letter, invalid
            else:                                                           # Player successfully revealed the full word
                print('You win!!')
                print('The answer is: ' + answer)
                break                                                       # Exit the game loop
        else:                                                               # Player failed within the allowed attempts
            print('You are completely hung :(')
            print('The answer is: ' + answer)
            break                                                           # Exit the game loop


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


if __name__ == '__main__':
    main()
