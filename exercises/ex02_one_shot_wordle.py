"""EX02 - One Shot Wordle, another step towards Wordle."""


__author__ = "730322060"

secret: str = str("python")
guess: str = input("What is your " + str(len(secret)) + "-letter guess? ")
i: int = 0
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
index: int = 0
emoji: str = str("")

while i <= len(secret):
    if len(guess) == len(secret):
        while index < len(secret):
            if guess[index] == secret[index]:
                emoji = emoji + GREEN_BOX
            else:
                character_exists: bool = False
                alt_index: int = 0
                while character_exists is False and alt_index < len(secret):
                    if guess[index] == secret[alt_index]:
                        character_exists = True
                    else:
                        alt_index = alt_index + 1
                if character_exists is True:
                    emoji = emoji + YELLOW_BOX
                else:
                    emoji = emoji + WHITE_BOX
            index = index + 1
        print(emoji)
        if guess == secret:
            print("Woo! You got it!")
        else:
            print("Not quite. Play again soon!")
        i = len(secret) + 1
    else:
        guess = input("That was not " + str(len(secret)) + " letters! Try again: ")