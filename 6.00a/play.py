###
import math
import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7
ASTERISK = '*'

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10, '*':0
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

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
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist
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
        
    num_asterisk=int(math.ceil(n / 7))
    for i in range(num_asterisk):
        x=random.choice(ASTERISK)
        hand[x]= hand.get(x, 0) + 1
        
    for i in range(num_vowels+1, n):    
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1    
    return hand


def substitute_hand(hand, letter):
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

hand = {'a':1, 'q':1, 'd':2, 'm':1, 'u':1, '*':1}
letter = 'A'
print(substitute_hand(hand, letter))

    
