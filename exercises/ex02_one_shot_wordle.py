"""EX02 - One Shot Wordle, another step towards Wordle"""


__author__ = "730322060"

secret: str = str("python")
guess: str = input("What is your " + str(len(secret)) + " letter guess? ")
i: int = len(guess)

index: int = 0
White_box: str = "\U00002B1C"
Green_box: str = "\U0001F7E9"
Yellow_box: str = "\U0001F7E8"
Emoji: str = ""
character_exists: bool = False
alternate_indices: int = 0


while i <= 6:
    if len(guess) == 6:
        if guess == secret:
            print("Woo! You got it!")
        else:
            print("Not quite. Play again soon!")
        i = i + 1
    else:
        guess: str = input("That was not " + str(len(secret)) + " letters! Try again: ")


while index < len(secret):
    if guess[index] == secret[index]:
        Emoji = Emoji + Green_box
    else:
        while alternate_indices < len(secret):
            if guess[index] == secret[alternate_indices]:
                character_exists is True
            else:
                alternate_indices = alternate_indices + 1
        if character_exists is True:
            Emoji = Emoji + Yellow_box
        else:
            Emoji = Emoji + White_box
    index = index + 1

print(Emoji)
