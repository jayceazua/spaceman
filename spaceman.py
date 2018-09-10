import random

def load_word():
    # open the file and read it
   f = open('words.txt', 'r')
   # read it per lines
   words_list = f.readlines()
   # close the file after
   f.close()
   # put each word into a list split by their space
   words_list = words_list[0].split(' ')
   # select random word from the words_list
   secret_word = random.choice(words_list)
   # return that secret_word
   return secret_word

def is_word_guessed(secret_word, letters_guessed):
    '''
    secretWord: string, the random word the user is trying to guess.  This is selected on line 9.
    lettersGuessed: list of letters that have been guessed so far.
    returns: boolean, True only if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    # iterate through the secret_word
    for letter in secret_word:
         # if the letter is not in the list of letters_guessed
         if letter not in letters_guessed:
             # return False and check again
             return False
    return True

def get_guessed_word(secret_word, letters_guessed):
    '''
    secretWord: string, the random word the user is trying to guess.  This is selected on line 9.
    lettersGuessed: list of letters that have been guessed so far.
    returns: string, of letters and underscores.  For letters in the word that the user has
    guessed correctly, the string should contain the letter at the correct position.  For letters
    in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''
    # FILL IN YOUR CODE HERE...
    # declare a variable with empty string to append
    word = ""
    # loop through secret_word and get individual letters from there
    for letter in secret_word:
        # if the letter from the secret_word is in the letters_guessed
        if letter in letters_guessed:
        # append it in the word variable
            word += letter + ""
        # if not append it with a underscore
        else:
            word += "_ "
    # return the word once we finish appending
    return word

def get_available_letters(letters_guessed):
    '''
    lettersGuessed: list of letters that have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # laziest way to convert a string into a list
    choices_left = list("abcdefghijklmnopqrstuvwxyz")
    # loop through the letters_guessed one letter at a time
    for letter in letters_guessed:
        # if the letter is in the choices_left
        if letter in choices_left:
            # remove it from the "list"
            choices_left.remove(letter)
    # return the choices_left after it removes everything from within
    return choices_left

def spaceman(secret_word):
    '''
    secretWord: string, the secret word to guess.

    Starts up a game of Hangman in the command line.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to guess one letter per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.
    '''
    # FILL IN YOUR CODE HERE...
    # get the length of the secret_word
    length_word = len(secret_word)
    # declare an empty list
    letters_guessed = []
    print("What is your name?")
    # get the name of the user
    user_name = raw_input('-> ')
    # print welcome message
    print("Welcome {}, to the Spaceman Game,".format(user_name))
    print("the word to guess is {} letters long.".format(length_word))

    # while the word is not guessed right continue to play the game
    while not is_word_guessed(secret_word, letters_guessed):
        print('Guess a letter that is in the word.')
        # capture the user's input of a single letter
        user_guess = raw_input('-> ')
        # if the user's input is not in the letters already guessed list
        if user_guess not in letters_guessed:
            # append the new letter into the list
            letters_guessed.append(user_guess)
            # if is_word_guessed(secret_word, letters_guessed) is not True:
            if not is_word_guessed(secret_word,letters_guessed):  # Idiomatic python example
                # display to the user the amount of letters left to guess
                print "Letter you have not guessed yet: {} ".format(get_available_letters(letters_guessed))
                # show the word with underscores and the correctletters in order
                print "You are still missing these letters {} ".format(get_guessed_word(secret_word, letters_guessed))
        else:
            # if the letter is in the letters guessed list print the following
            print('Guess another letter that you have not chosen yet.')
    else:
        # once the loop returns False print the message that the user won
        print('You won! the word was {}'.format(secret_word))


# Future developments:
# >> need to have edge cases:
### 1. limit the amount of turns
### 2. exit if the user reaches their max turns allowed.
### 3. allow the user to guess the complete word if given the chance
### 4. once the user wins or losess allow for the user to reset the game
# >> nice to have edge cases
### Edge Case: did the user actually put in one letter and is it a letter or charater


secret_word = load_word()
spaceman(load_word())
