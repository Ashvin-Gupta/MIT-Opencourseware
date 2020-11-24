# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    points = 0
    secret_word_array = list(secret_word)

    for letter in secret_word_array:
        if letter in letters_guessed:
            points += 1
            if points == len(secret_word):
                return True
        else:
            return False


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    secret_word_array = list(secret_word)
    secret_word_copy = secret_word_array[:]
    i =0

    for letter in secret_word_copy:
        if letter not in letters_guessed:
            secret_word_array[i] = "_ "
        i += 1

    guessed_word = ''.join(secret_word_array)

    return guessed_word




def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    alphabet  = list(string.ascii_lowercase)
    alphabet_copy = alphabet[:]
    i = 0

    for letter in alphabet_copy:
        if letter in letters_guessed:
            alphabet.remove(letter)

    remaining_letters = ''.join(alphabet)

    return remaining_letters


    
    
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    print("Welcome to the game of Hangman!")
    word_length = len(secret_word)
    print(f"I am thinking of a word which is {word_length} letters long.")
    guesses = 12
    print(f"You have {guesses} guesses left.")
    letters_guessed = []
    print("Available letter: ", get_available_letters(letters_guessed))
    end = 0
    counter = 0
    warnings  = 3

    while (guesses> 0):
        letters_guessed.append(input("Please guess a letter: ").lower())

        if str.isalpha(''.join(letters_guessed)) == False:
            print(f"That is not a vailid letter. You have {warnings} warnings left.")
            warnings = warnings - 1
            if warnings == 0:
                guesses = guesses - 1
        else:
            if letters_guessed[counter] in secret_word:
                print("Good guess: ", get_guessed_word(secret_word, letters_guessed))
                if is_word_guessed(secret_word, letters_guessed) == True:
                    print("Well done! You guessed my word!")
                    score  = guesses*len(secret_word)
                    print("Your total score for this game is : ", score)
                    break

                else:
                    print(f"You have {guesses} left.")
            else:
                print("Oops! That letter is not in my word: ", get_guessed_word(secret_word, letters_guessed))
                if letters_guessed[counter] in ['a', 'e', 'i', 'o', 'u']:
                    guesses = guesses - 2
                else:
                    guesses = guesses - 1
                print(f"You have {guesses} left.")

            counter += 1
            print(get_available_letters(letters_guessed))
            print("-----------------")

    if guesses == 0:
        print("Sorry, you ran out of guesses. My word was", secret_word)
    



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"


    if len(my_word) != len(other_word):
        return False

    my_word = list(my_word)
    other_word = list(other_word)
    points = 0

    without_spaces = my_word.strip()
    for letter in without_spaces:
        if letter in other_word:
            points += 1
    if points == len(without_spaces):
        return True






def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    possible_matches = []
    
    for word in wordlist:
        if match_with_gaps(my_word, word) == True:
            possible_matches.append(word)
    
    print(possible_matches)
    



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    secret_word = choose_word(wordlist)
    hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)
