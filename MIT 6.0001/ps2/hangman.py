
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

    found = 0
    word = list(secret_word)

    for i in letters_guessed:
        for n in range(len(secret_word)):
            if secret_word[n] == i:
                found += 1
                word.remove(i)
    if found == len(secret_word):
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

    word = list(secret_word)
    a = 0
    found_str = ""
    found = ["_ "] * len(secret_word)
    for i in letters_guessed:
        while a < len(secret_word):
            if word[a] == i:
                found[a] = i
            a += 1
        a = 0
    for i in found:
        found_str += i
    return found_str

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    letters = ""
    letters_list = list(string.ascii_lowercase)
    for i in letters_guessed:
        if i in letters_list:
            letters_list.remove(i)

    for i in letters_list:
        letters += i
    return letters
    

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
    word = choose_word(wordlist)
    guesses = 6
    letters_guessed = []
    warnings = 3
    print("Welcome to the game Hangman !")
    print("I am thinking of a word that is", len(word), "letters long.")
    print("You have 3 warnings left")
    print("-" * 12)
    track = 0
    letter = ""

    while not (is_word_guessed(word,letters_guessed)) and guesses > 0:
        print("You have", guesses, "guesses" if guesses > 1 else "guess")
        print("Avaliable letters:",get_available_letters(letters_guessed))
        letter = input("Please guess a letter:")
        letter = letter.lower()
        past_guesses = get_available_letters(letters_guessed)
        if not (letter.isalpha()):
            if warnings <= 0:
                print("You do not have any warnings left, you lost a guess")
                guesses -= 1
            else:
                warnings -= 1
                print("Oops! That is not a valid letter. You have ", warnings, "warnings" if warnings > 1 else "warning", "left")
        elif not(letter in past_guesses):
            if warnings <= 0:
                print("You do not have any warnings left, you lost a guess")
                guesses -= 1
            else:
                warnings -= 1
                print("Oops! You made that guess before, you lost a warning ", warnings,"warnings" if warnings > 1 else "warning", "left")
        else:
            if not letter.islower():
                letter = letter.lower()
            letters_guessed.append(letter)
            if letter in word:
                print("Good guess:", get_guessed_word(word,letters_guessed))
            else:
                print("Oops! That letter is not in my word:",get_guessed_word(word,letters_guessed))
                if letter  in "aeiou":
                    print("You made a vowel letter guess and vowel not in secret word so you lost 2 guesses")
                    guesses -= 2
                else:
                    guesses -= 1
        print("-" * 12)
    if  not is_word_guessed(word, letters_guessed):
        print("You run out of guesses , so lost the game.The words was :", word)
    else:
        print("Congrulatíons , you won the game with", len(set(word)) * guesses, "total score")




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
    temp_myword = my_word.replace(" ","")
    found = 0
    if not len(temp_myword) == len(other_word):
        return False

    for i in range(len(other_word)):
        if temp_myword[i] == other_word[i]:
            found += 1
        elif temp_myword[i] == "_":
            if other_word[i] not in temp_myword:
                found += 1

    if(found == len(temp_myword)):
        return True
    else:
        return False



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
    file = open("words.txt", "r")
    matches = 0
    for word in file.read().split():
        if match_with_gaps(my_word,word):
            matches += 1
            print(word, end=" ")
    if matches == 0:
        print("No matches found", end= " ")



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
    word = choose_word(wordlist)
    guesses = 6
    letters_guessed = []
    warnings = 3
    print("Welcome to the game Hangman !")
    print("I am thinking of a word that is", len(word), "letters long.")
    print("You have 3 warnings left")
    print("-" * 12)
    track = 0
    letter = ""

    while not (is_word_guessed(word,letters_guessed)) and guesses > 0:
        print("You have", guesses, "guesses" if guesses > 1 else "guess")
        print("Avaliable letters:",get_available_letters(letters_guessed))
        print("if you want to see possible matches from file enter '*'")
        print(get_guessed_word(word, letters_guessed))
        letter = input("Please guess a letter:")
        if(letter == "*"):
            print("Possible word matches are:")
            show_possible_matches(get_guessed_word(word, letters_guessed))
            print()
        else:
            letter = letter.lower()
            past_guesses = get_available_letters(letters_guessed)
            if not (letter.isalpha()):
                if warnings <= 0:
                    print("You do not have any warnings left, you lost a guess")
                    guesses -= 1
                else:
                    warnings -= 1
                    print("Oops! That is not a valid letter. You have ", warnings, "warnings" if warnings > 1 else "warning", "left")
            elif not(letter in past_guesses):
                if warnings <= 0:
                    print("You do not have any warnings left, you lost a guess")
                    guesses -= 1
                else:
                    warnings -= 1
                    print("Oops! You made that guess before, you lost a warning ", warnings,"warnings" if warnings > 1 else "warning", "left")
            else:
                if not letter.islower():
                    letter = letter.lower()
                letters_guessed.append(letter)
                if letter in word:
                    print("Good guess:", get_guessed_word(word,letters_guessed))
                else:
                    print("Oops! That letter is not in my word:",get_guessed_word(word,letters_guessed))
                    if letter in "aeiou":
                        print("You made a vowel letter guess and vowel not in secret word so you lost 2 guesses")
                        guesses -= 2
                    else:
                        guesses -= 1
        print("-" * 12)

    if  not is_word_guessed(word, letters_guessed):
        print("You run out of guesses , so lost the game.The words was :", word)
    else:
        print("Congrulatíons , you won the game with", len(set(word)) * guesses, "total score")





if __name__ == "__main__":

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    #secret_word = choose_word(wordlist)
    #hangman(secret_word)
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines.
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
