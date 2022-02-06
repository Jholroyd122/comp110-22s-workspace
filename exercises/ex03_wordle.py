"""EX03 - Structured Wordle, Another step toward the full Wordle game."""


__author__ = "730322060"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def contains_char(word: str, character: str) -> bool:
    """Searches through the guessed word to see if a charcter matches."""
    assert len(character) == 1
    character_exists: bool = False
    index: int = 0
    while character_exists is False and index < len(word):
        if word[index] == character:
            character_exists is True
            return True
        else:
            index = index + 1
            
    return False


def emojified(secret: str, guess: str) -> str:
    """Given a guess and a secret word, returns a string of emojis indicating which letters are correct."""
    assert len(guess) == len(secret)
    emoji: str = ""
    i: int = 0
    while i < len(secret):
        if contains_char(guess, secret[i]) is False:
            emoji = emoji + WHITE_BOX
        else:
            if contains_char(guess, secret[i]) is True:
                if guess[i] == secret[i]:
                    emoji = emoji + GREEN_BOX
                else:
                    emoji = emoji + YELLOW_BOX
        i = i + 1
    
    return emoji


def input_guess(expected_length: int) -> str:
    user_guess: str = input(f"Enter a {expected_length} letter word: ")
    while len(user_guess) != expected_length:
        user_guess = input(f"That wasn't {expected_length} characters! Try again: ") 

    return user_guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret_word: str = "codes"
    turn: int = 1
    won: bool = False
    while turn <= 6 and won is False:
        win_message: str = str(f"You won in {turn}/6 turns!")
        print(f"=== Turn {turn}/6 ===")
        input: str = input_guess(len(secret_word))
        print(emojified(secret_word, input))
        if input == secret_word:
            won = True
            print(win_message)
        turn = turn + 1
    if won is False:
        print("X/6 - Sorry, try again tommorow!")


if __name__ == "__main__":
    main()