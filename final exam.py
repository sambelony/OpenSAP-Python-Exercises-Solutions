# Wordle in Python
#
# Your task for the final assignment is to implement a Wordle clone in Python.
# The basis for your version of Wordle is the file 5_letter_words.txt [1].
# It contains more than 5.700 five letter words. In order to build your version
# of Wordle perform the following steps:
#
# Implement a function word_list() that reads the 5_letter_words.txt file
# and returns a list of the words in the file.
# Implement a function random_word() that takes a list of words as a parameter
# and returns a random word from this list.
# Implement a function is_real_word() that takes two parameters, a guess and
# a word list and returns True if the word is in the word list and False otherwise.
# Implement a function check_guess()that takes two parameters.
# The first is the guessed word and the second is the word the user has to find.
# check_guess() returns a string containing the following characters:
# X for each character in the guess that is at the correct position.
# O for each character in the guess that is in the word but not at the correct position.
# _ for each character in the guess that is not part of the word.
# For example, check_guess("birds", "words") should return __XXX.
# If a letter is used twice in the guessed word and exists only once in the word to be found,
# then only one letter in the return string is marked.
# In case one of the two letters is positioned correctly, then this letter is marked with an X in the return string.
# For example, check_guess("carat", "train") should return _OO_O.
# Another example, check_guess("taunt", "train") should return XO_O_
# Implement a function next_guess() that takes a word list as a parameter.
# The function asks the user for a guess, converts the guess to lower case and checks if the guess is in the word list.
# If this is the case, the guess is returned. Otherwise, the function asks the user for another guess.
# Implement a function play() that:
# Uses the functions word_list and random_word to select a random 5 letter word.
# Asks the user for a guess using the next_guess function.
# Checks each guess using the check_guess function and shows the result to the user.
# Checks if the users guessed the right word with six guesses or less.
# If yes, the user wins and the function prints You won!. Otherwise the user loses and the function prints You lost!
# as well as The word was: followed by word the user had to find.

import random

def word_list():
    with open("5_letter_words.txt", 'r') as f:
        word_list = [line.strip() for line in f]
    return(word_list)

def random_word(word_list):
    return word_list[random.randrange(len(word_list))]

def is_real_word(guess, word_list):
    return guess in word_list

def check_guess(guess, random_word):
    a_string = ""
    a_elements = []
    for c in range(len(guess)):
        if guess[c] == random_word[c]:
            a_string += "X"
        elif guess[c] in random_word and guess[c] not in a_elements or guess.count(guess[c]) == random_word.count(guess[c]) > 1:
            a_string += "O"
        else:
            a_string += "_"
        a_elements.append(guess[c])
    return a_string

def next_guess(word_list):
    flag_on = True
    while flag_on:
        guess = input("Please enter a guess:").lower()
        if is_real_word(guess, word_list):
            flag_on = False
        else:
            print("That's not a real word!")
    return guess

def play():
    word_list_var = word_list()
    random_word_var = random_word(word_list_var)
    count = 0
    while count < 6:
        guess = next_guess(word_list_var)
        if check_guess(guess, random_word_var) == "XXXXX":
            print(check_guess(guess, random_word_var))
            print("You Won!")
            break
        elif count < 5:
            print(check_guess(guess, random_word_var))
            count += 1
        else:
            print(check_guess(guess, random_word_var))
            print("You Lost!")
            print("The word was:", random_word_var)
            break
