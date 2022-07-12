import random
from words import words
import string
from hangman_visual import lives_visual_dict

def get_valid_word(words):
    word = random.choice(words) # randomly chooses a word from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # what the user has guessed

    lives = 8

    # getting user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        # ' '.join([ 'a', 'b', 'cd' ]) --> 'a b cd' (joined separated by a space)
        print(f'You have {lives} lives left and have used these letters: ', ' '.join(used_letters))

        # what current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(lives_visual_dict[lives])
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')
            else:
                lives = lives - 1 # takes away a life if wrong
        elif user_letter in used_letters:
            print('\nYou have already guessed that character. Please try again.')
        else:
            print('\nInvalid character. Please try again.')
    # gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print(lives_visual_dict[lives])
        print('You died, sorry. The word was', word)
    else:
        print(f'You have guessed the word, {word}!!')

hangman()
