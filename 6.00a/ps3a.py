# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 07:17:49 2017

@author: KAMALDEEN
"""

import math
import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
ASTERISK = '*'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10, '*':0
}

WORDLIST_FILENAME = "words3.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    
#    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
#    print("  ", len(wordlist), "words loaded.")
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq

def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    You may assume that the input word is always either a string of letters, 
    or the empty string "". You may not assume that the string will only contain 
    lowercase letters, so you will have to handle uppercase and mixed case strings 
    appropriately. 

	The score for a word is the product of two components:

	The first component is the sum of the points for letters in the word.
	The second component is the larger of:
            1, or
            7*wordlen - 3*(n-wordlen), where wordlen is the length of the word
            and n is the hand length when the word was played

	Letters are scored as in Scrabble; A is worth 1, B is
	worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string
    n: int >= 0
    returns: int >= 0
    """
    wordlen=len(word)
    word=str.lower(word)
    partial_score=0
    for letters in word:
        partial_score=partial_score+SCRABBLE_LETTER_VALUES[letters]            
    half_score_test=(7*wordlen)-3*(n-wordlen)
    if half_score_test > 1:
        half_score=half_score_test
    else:
        half_score= 1    
    total_score=partial_score*half_score
    return(total_score)

def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter, end=' ')      # print all on the same line
    print()                              # print an empty line

def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS (note,
    ceil(n/3) means the smallest integer not less than n/3).

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    
    hand={}
    num_vowels = int(math.ceil(n / 4))

    for i in range(num_vowels):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1
        
    num_asterisk=int(math.ceil(n / HAND_SIZE))
    for i in range(num_asterisk):
        x=random.choice(ASTERISK)
        hand[x]= hand.get(x, 0) + 1
        
    for i in range(num_vowels+1, n):    
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1    
    return hand
 
def update_hand(hand, word):
    """
    Does NOT assume that hand contains every letter in word at least as
    many times as the letter appears in word. Letters in word that don't
    appear in hand should be ignored. Letters that appear in word more times
    than in hand should never result in a negative count; instead, set the
    count in the returned hand to 0 (or remove the letter from the
    dictionary, depending on how your code is structured). 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    word=str.lower(word)
    new_hand=hand.copy()
    for letterz in word:
        if letterz in new_hand.keys():
            new_hand[letterz]=new_hand.get(letterz,0)-1
            if new_hand[letterz]<1:
                del(new_hand[letterz])
    return(new_hand)

def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
   
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    """
    word=str.lower(word)
    temp_hand=hand.copy()
    validator=False
    if word in word_list:
        validator=True
    elif '*' in word:
        for alphab in VOWELS:
            new_word = word.replace('*',alphab)
            #str.lower(new_word)
            if new_word in load_words():
                validator=True
                break                                        
    for leta in word:
        if leta not in temp_hand.keys():
            validator=False
        elif leta in hand:
            temp_hand[leta]=temp_hand.get(leta,0)-1
            if temp_hand[leta]<1:
                del(temp_hand[leta])
    return(validator)

def calculate_handlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    mylist=[]
    for keys in hand:
        mylist.append(hand[keys])
    hand_length=sum(mylist)
    return(hand_length)

def play_hand(hand, word_list):

    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    
    * The user may input a word.

    * When any word is entered (valid or invalid), it uses up letters
      from the hand.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing two 
      exclamation points (the string '!!') instead of a word.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      returns: the total score for the hand
      
    """
    sum_score=0
    while hand != {}:
        print('Current Hand:  ')
        display_hand(hand)
        word=input('Enter word, or "!!" to indicate that you are finished:')
        word=str.lower(word)
        if word=='!!':break
        if is_valid_word(word, hand, word_list) == True:
            n = calculate_handlen(hand)
            word_score=get_word_score(word, n)
            print(word,'earned',word_score,'points')
            sum_score=sum_score + word_score
            print('TOTAL: ',sum_score)
        else:
            print('That is not a valid word. Please choose another word.')
        hand=update_hand(hand, word)
    total_score=sum_score
    print('Ran out of letters. total score for this hand: ',total_score)
    return(total_score)
    
def substitute_hand(hand, letter):
    """ 
    Allow the user to replace all copies of one letter in the hand (chosen by user)
    with a new letter chosen from the VOWELS and CONSONANTS at random. The new letter
    should be different from user's choice, and should not be any of the letters
    already in the hand.

    If user provide a letter not in the hand, the hand should be the same.

    Has no side effects: does not mutate hand.

    For example:
        substitute_hand({'h':1, 'e':1, 'l':2, 'o':1}, 'l')
    might return:
        {'h':1, 'e':1, 'o':1, 'x':2} -> if the new letter is 'x'
    The new letter should not be 'h', 'e', 'l', or 'o' since those letters were
    already in the hand.
    
    hand: dictionary (string -> int)
    letter: string
    returns: dictionary (string -> int)
    """
    letter=str.lower(letter)
    if letter in hand.keys():
        def choice_letter(hand):
            choice = True
            english_alphabets = string.ascii_lowercase
            while choice ==True:
                x = random.choice(english_alphabets)
                if x not in hand.keys():
                    choice=False
            return(x)
        new_letter=choice_letter(hand)
        for i in range (hand[letter]):
            hand[new_letter]=hand.get(new_letter,0)+ 1
        del(hand[letter])
    else:
        print('sorry,the letter is not in your current hand')
    return(hand)
    
    
def play_game(word_list):
    """
    Allow the user to play a series of hands

    * Asks the user to input a total number of hands

    * Accumulates the score for each hand into a total score for the 
      entire series
 
    * For each hand, before playing, ask the user if they want to substitute
      one letter for another. If the user inputs 'yes', prompt them for their
      desired letter. This can only be done once during the game. Once the
      substitue option is used, the user should not be asked if they want to
      substitute letters in the future.

    * For each hand, ask the user if they would like to replay the hand.
      If the user inputs 'yes', they will replay the hand and keep 
      the better of the two scores for that hand.  This can only be done once 
      during the game. Once the replay option is used, the user should not
      be asked if they want to replay future hands. Replaying the hand does
      not count as one of the total number of hands the user initially
      wanted to play.

            * Note: if you replay a hand, you do not get the option to substitute
                    a letter - you must play whatever hand you just had.
      
    * Returns the total score for the series of hands

    word_list: list of lowercase strings
    """
    subst = 0
    replay=0
    final_score = 0
    hands_played = input('Enter total number of hands: ')
    hands_played = int(hands_played)
    for h in range(hands_played):
        if input=='done':break
        hand=deal_hand(HAND_SIZE)
        display_hand(hand)
        if subst == 0:
            substitute=input('Would you like to substitute a letter? ')
            str.lower(substitute)
            if substitute =='yes':
                letter = input('Which letter would you like to replace: ')
                str.lower(letter)
                subst = 1
                substitute_hand(hand, letter)
                display_hand(hand)
            else:
                subst = 0
        small_play=play_hand(hand, word_list)
        int(small_play)
        print('------------------')
        if replay==0:
            replay_hand=input('Would you like to replay the hand?')
            print('-------------------')
            str.lower(replay_hand)
            if replay_hand == 'yes':
                replay=1
                alt_play=play_hand(hand, word_list)
                if alt_play > small_play:
                    small_play = alt_play
                    print('-------------------')
            else:
                replay=0
        final_score +=small_play
        print('-------------------')
    print('Total score over all hands:', final_score)
    return(final_score)


if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)
    
    
    
    #########################
    ##############


	
