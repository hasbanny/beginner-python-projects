from random import shuffle


def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]


# variable to keep the game going if the user wants
play = True

# 1. read in file with random words
f = open("random_words", "r")
if f.mode == "r":
    word_list = f.read().splitlines()
    print(word_list)

while play is True:
    # variables go in the loop in order to reset their value in each 'game'
    # setting the limit of guesses
    guess_limit = 5
    # boolean to see if the word is discovered
    word_discovered = False
    # random word chosen from file
    chosen_w = ''
    # incognito word
    incognito_word = ''

    # 2. ask user for size input
    word_size = input("What size of word would you like? ")
    # search through the list of words to find a word of that size

    for word in word_list:
        if len(word) == int(word_size):
            chosen_w += word + '\n'
    select_words = chosen_w.splitlines()

    # randomizing the selected words
    shuffle(select_words)
    word_to_guess = select_words[0]
    print(word_to_guess)

    # start the guessing game
    incognito_word = '*' * int(word_size)
    print(f"Start guessing!\nWord: {incognito_word}")

    while guess_limit != 0 and word_discovered is False:
        guess = input("Guess: ")

        if guess in word_to_guess:
            print(f"{guess} is in the word!")
            idx = find(word_to_guess, guess)
            for i in idx:
                incognito_word = incognito_word[:i] + guess + incognito_word[i + 1:]
            if '*' not in incognito_word:
                word_discovered = True
        else:
            print(f"{guess} is NOT in the word!")
            guess_limit -= 1
            print(f"Only {guess_limit} tries left.")

        print(f"Word: {incognito_word}")

    if word_discovered is True:
        print(f"Congrats! You guessed the word with {guess_limit} tries left!")
    else:
        print(f"You're out of tries! The word was {word_to_guess}.")

    answer = input("Would you like to play again? Y/N: ")
    if answer == 'N':
        play = False
        print("Game over.")