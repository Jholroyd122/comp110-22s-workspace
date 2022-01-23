"""EX01 - Chardle - A Cute Step towards Wordle"""


_author_ = "730322060"

five_character_word = str = str(input("Enter a 5-character word: "))
if len(five_character_word) != 5:
    print("Error: Word must contain 5 letters.")
    exit()
single_character = str = input("Enter a single character: ")
if len(single_character) != 1:
    print("Error: Character must be a single character.")
    exit()
matching_indices = int = five_character_word.count(single_character)
print("Searching for " + single_character + " in " + five_character_word)


if single_character == five_character_word[0]:
    print(single_character + " found at index 0. ")
if single_character == five_character_word[1]:
    print(single_character + " found at index 1. ")
if single_character == five_character_word[2]:
    print(single_character + " found at index 2. ")
if single_character == five_character_word[3]:
    print(single_character + " found at index 3. ")
if single_character == five_character_word[4]:
    print(single_character + " found at index 4. ")

if matching_indices == 0:
    print("no instance of " + single_character + " found in " + five_character_word)
if matching_indices == 1:
    print("1 instance of " + single_character + " found in " + five_character_word)
if matching_indices == 2:
    print("2 instance of " + single_character + " found in " + five_character_word)
if matching_indices == 3:
    print("3 instance of " + single_character + " found in " + five_character_word)
if matching_indices == 4:
    print("4 instance of " + single_character + " found in " + five_character_word)
if matching_indices == 5:
    print("5 instance of " + single_character + " found in " + five_character_word)
