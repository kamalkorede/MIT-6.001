# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 20:45:00 2017

@author: KAMALDEEN
"""

import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    """    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    line = inFile.readline()
    wordlist = line.split()
    return wordlist
wordlist = load_words()

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)
#wrd=print(choose_word(wordlist))

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    lists=[]
    sub_secret=secret_word[:]
    for letters in sub_secret:
        if letters not in lists:
            lists.append(letters)
    guess_left=6
    lst=[]
    while True:
        letters_guessed=input('Enter your guess: ',)
        if letters_guessed in lst:
            guess_left-=1
        elif letters_guessed in secret_word:
            lst.append(letters_guessed)
        else:
            guess_left-=1
        if guess_left==0:break
        if (secret_word==lst or set(secret_word).issubset(lst)):break
    letters_guessed=lst
    print('secret word is: ',secret_word)
    return secret_word==letters_guessed or set(secret_word).issubset(letters_guessed)        


def alphabets():
    '''all letters in english alphabet'''
    return(string.ascii_lowercase)


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    rep=('_ ')*len(secret_word)
    print('Guess the secret word: ',rep)
    lists=[]
    secret_wrd=secret_word[:]
    for letters in secret_wrd:        
        if letters not in lists:
            lists.append(letters)
#    sub_secret=lists
    guess_left=6
    warning=0
    lst=[]
    all_guessed=[]
    atoz=string.ascii_lowercase
    while True:
        secret_wrd=secret_word[:]
        letters_guessed=input('Enter your guess(only 1 guess at a time): ',)
        str.lower(letters_guessed)
        if str.isalpha(letters_guessed)==False:
            warning+=1
            print('invalid input!')
            print('you have',(3-warning),'warnings left')
        all_guessed.append(letters_guessed)
        for leter in atoz:
            if leter in all_guessed:
                atoz=atoz.replace(leter,'_')
        print('remaining letters yet to be guessed: ',atoz)               
        if letters_guessed in lst:
            guess_left-=1
        elif letters_guessed==secret_word:
            print('your guess was perfect!,YOU WON!')
            break            
        elif letters_guessed in secret_word:
            lst.append(letters_guessed)
            print('That was a pretty good guess')
        else:
            print('your guess was wrong')
            guess_left-=1
        print('you have',guess_left,'guesses left')
        for alpha in secret_wrd:
            if alpha not in lst:
                secret_wrd=secret_wrd.replace(alpha,' _ ') 
        print(secret_wrd)
        print('-------------')
        if (secret_word==lst or set(secret_word).issubset(lst)):
            print('YOU WON!')
            break
        if guess_left==0:
            print('Sorry,you lost!')
            print('The correct word is:',secret_word)
            break
        if warning==3:
            print('you have no warning left,Game Over!')
            break
    letters_guessed=lst
#    print('secret word is: ',secret_word)
    print('would you like to play again?')
    return (secret_wrd)


def hangman(secret_word):
    print('Welcome to the game Hangman!')
    print('I am thinking of a word',len(secret_word),'letters long.')
    print('You have 6 guess(es) left.')
    letters_guessed=None    
    get_guessed_word(secret_word, letters_guessed)
    print('*********************')
    return('endgame')


secret_word=choose_word(wordlist)
play=hangman(secret_word)


    
    #####