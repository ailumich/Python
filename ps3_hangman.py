# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
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

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    count = 0
    for char in secretWord:
        if char in lettersGuessed:
            count += 1
    return count == len(secretWord)


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    word = ""
    for char in secretWord:
        if char in lettersGuessed:
            word += char
        else:
            word += "_ "
    return word



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    all_letters = string.ascii_lowercase
    for letter in lettersGuessed:
        all_letters = all_letters.replace(letter,'')
    return all_letters
    
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    print("Welcome to Hangman")
    print("The word is "+str(len(secretWord))+" letters long")
    lettersGuessed = []
    numguess = 8
    while numguess >= 0:
        if numguess == 0:
            print('_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\n')
            print("Sorry you ran out of guesses. The word is "+secretWord)
            break
        else:
            print("You have "+str(numguess)+" guesses left")
            print("Available letters: "+str(getAvailableLetters(lettersGuessed)))
            value = input("Please guess a letter: ")
            if value in lettersGuessed:
                print("Oops! You guessed that: "+getGuessedWord(secretWord,lettersGuessed))
            elif value in secretWord:
                lettersGuessed += value
                print("Good guess: "+getGuessedWord(secretWord,lettersGuessed))
                if isWordGuessed(secretWord,lettersGuessed) == bool('True'):
                    print('_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\n')
                    print("Congratulations, you won!")
                    break 
            else:
                lettersGuessed += value
                print("Bad letter: "+getGuessedWord(secretWord,lettersGuessed))            
        numguess -= 1
            
# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
