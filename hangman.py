from random import choice as r

# Function updates the users current guess " _ _ _" to "R _ _"
def updateGuess(letter, guess, correct_word):
    index_of_word = []
    index = 0
    # strings are immuatable, so turn into list
    temp_list = list(guess)
    # get the index of the string that corresponds to guessed letter
    while index < len(correct_word):
        if letter == correct_word[index]:
            index_of_word.append(index)
        index += 1
    underscore_index = 0
    for x in temp_list:
        if x != ' ':
            if underscore_index in index_of_word:
                temp_list[underscore_index*2] = letter
            underscore_index += 1
    return "".join(temp_list)

# The set up
lives = 5
letter_bank = []
# The topics
Names = ["erika", "erik", "jessica", "clayton"]
Colors = ["purple", "pink", "amethyst", "crimson"]
Animals = ["rhinoceros", "giraffe", "flamingo", "chicken"]

# The list of topics
themes_strings = ["Colors", "Animals", "Names"]
themes_lists = [Colors, Animals, Names]

user_theme = ""
user_theme = input(f"Welcome to hangman! Pick a topic from the following list: \n {themes_strings} \n")
while user_theme not in themes_strings:
    print("That's not a valid theme, please enter a valid theme")
    user_theme = input()

# Getting the index for themes_lists, there's got to be a better way to do this...
theme_index = 2
if user_theme == "Colors":
    theme_index = 0
elif user_theme == "Animals":
    theme_index = 1

correct_word = r(themes_lists[theme_index])
# print(correct_word)
victory_len = len(correct_word) # Win condition when len(word) = 0
victory = False
current_guess = ""
hint = False # Let the user ask for a hint

# SETTING UP THE PRINTED GUESS IN FORMAT OF-> "_ _ _ _ _"
###############
for letter in correct_word:
    if letter == ' ':
        current_guess += '  '
        continue
    current_guess += '_ '

print("\n")
print(current_guess)
################

# The loop for the main game
while lives != 0:
    print(f"\n\nCurrent letter bank: \n{letter_bank}")
    user_letter =  input("Choose a letter: ")
    user_letter = user_letter.lower()
    if user_letter in letter_bank:
        user_letter = input("You already used this letter. Pick another letter: ")
        user_letter.lower()
        continue
    letter_bank.append(user_letter)

    if user_letter in correct_word:
        current_guess = updateGuess(user_letter, current_guess, correct_word)
        victory_len -= 1
        print(current_guess)
        input("Press enter to continue ")
        if victory_len == 0:
            victory = True
            break
    else:
        lives -= 1
        print(f"\n{user_letter} is not part of the word.\n{lives} lives remaining")
        input("Press enter to continue ")
    
    

if victory:
    print("\nYOU WON! (:")
else:
    print("\nYou lost ):")
