# 6.0001 Problem Set 3
#
# The 6.0001 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
#
# Name          : <Goktug AYAR>

import math
import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10, '*': 0
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

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	

def get_word_score(word, n):
    word_len = len(word)
    points = 0
    word = word.lower()
    second = 0
    value = (7 * word_len - 3*(n - word_len))
    for i in word:
        points += SCRABBLE_LETTER_VALUES[i]

    if value > 1:
        second = value
    else:
        second = 1
    return points*second


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
    num_vowels = int(math.ceil(n / 3))
    hand["*"] = 1
    for i in range(1,num_vowels):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1
    
    for i in range(num_vowels, n):    
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
    new_hand = hand.copy()
    new_word = word.lower()

    for i in new_word:
        if i in new_hand:
            if new_hand[i] > 1:
                new_hand[i] -= 1
            else:
                del new_hand[i]

    return new_hand




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
    temp_word = word.lower()
    temp_hand = hand.copy()
    temp_word_list = list(temp_word)


    for i in temp_word:
        if i in temp_hand:
            if temp_hand[i] > 1 and not i == "*":
                temp_hand[i] -= 1
            elif not i == "*":
                del temp_hand[i]
        else:
            return False

    if temp_word in word_list:
        return True
    temp_str = ""

    if "*" in temp_word:
        for i in VOWELS:
            temp_word_list[temp_word.find("*")] = i
            for item in temp_word_list:
                temp_str += item
            if temp_str in word_list:
                return True
            temp_str = ""
    return False




def calculate_handlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    count = 0
    for i in hand:
        count += hand[i]
    return count


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

    total_points = 0
    temp_hand = hand.copy()
    tempScore = 0
    user_out = False
    empty_list = False

    while True:
        print("Current hand : ", end=" ")
        display_hand(temp_hand)
        word = input("Enter word, or '!!' to indicate that you are finished:")
        if word == "!!":
            user_out = True
            break
        if is_valid_word(word, temp_hand, word_list):
            tempScore = get_word_score(word, HAND_SIZE)
            total_points += tempScore
            print('"', word, '"', "earned", tempScore, "points. Total:", total_points, "points")
        else:
            print("That is not a valid word. Please choose another world")
        temp_hand = update_hand(temp_hand, word)
        if not temp_hand:
            empty_list = True
            break

    if empty_list:
         print("Ran out of letters. Total score:", total_points)
         print()
    elif user_out:
        print('Total score:', total_points)
        print()
    return total_points



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
    if letter in hand:
        new_str = VOWELS + CONSONANTS
        key = hand.get(letter)
        del hand[letter]
        hand[random.choice(new_str)] = key

    return hand
       
    
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
    number_hands = int(input("Enter total number of hands:"))
    total_score = 0
    score = 0
    replay = "no"
    i = 0
    temp_score = 0
    flag = 0
    while i < number_hands:
        if replay == "no":
            hand = deal_hand(HAND_SIZE)
            print("Current hand", end=" ")
            display_hand(hand)
            choice = input("Would you like to substitute letter?(Yes or no, other than yes/no will be counted as 'no')")
            if choice == "yes":
                letter = input("Which letter would you like to replace.(Type the letter)")
                substitute_hand(hand, letter)

        score = play_hand(hand, word_list)
        total_score += score
        if flag == 0:
            temp_score = score
        if flag < 1:
            replay = input("Would you like to replay the hand?")
        if replay == "yes" and flag < 1:
            flag += 1
            i -= 1
        if temp_score > score:
            total_score -= score
        elif temp_score < score:
            total_score -= temp_score

        i += 1

    return total_score



if __name__ == '__main__':
    word_list = load_words()
    total_score = play_game(word_list)
    print()
    print("Total score over all hands", total_score)


    #hand = deal_hand(HAND_SIZE)
   # hand = {"a": 1,"c": 1,"f": 1,"i": 1,"*": 1,"t": 1,"x": 1}
    #play_hand(hand, word_list)
