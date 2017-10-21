# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 21:36:26 2017

@author: Don Gass
"""  
word = 'onomatopoeia'

def hangman(num_guesses, word):
    """
    Controls the logic of the hangman game.
    Handles the guesses and determines whether the user wins or loses.
    Calls hidden_word(word, guesses) to get the hidden word string with
    correctly guessed letters indicated. Eg. onom--opo--i-
    """
    guesses = ""
    print('\nYou have %d guesses. The word has %d letters.' % \
         (num_guesses, len(word))) 
    while len(guesses) < num_guesses:
        guess = input('Enter guess (#%d): ' % (len(guesses)+ 1))
        if len(guess) < 1 or len(guess) > 1:
            print('You must enter a single letter! Please try again')
            continue
        else:
            guesses += guess
            result = hidden_word(word, guesses)
            print(result)
            if '-' not in result:
                print('Congratulations! You guessed the word: ', word)
                return None
    print('You did not guess the word: ', word)

def hidden_word(word, guesses):
    """
    Takes in the word and string of guessed letters and returns a formatted
    hidden word string.
    """
    hidden_word = ""
    for letter in word:
        if letter in guesses:
            hidden_word += letter
        else:
            hidden_word += '-'
    return hidden_word

hangman(10, word)
