import itertools
import string
import sys
import time


def contains_digits(password: str) -> bool:
    """Check if a password contains digits."""
    return any(char in string.digits for char in password)


def contains_symbols(password: str) -> bool:
    """Check if a password contains symbols."""
    return any(char in string.punctuation for char in password)


def common_guess(word: str):
    """Checks a file filled with common words."""
    with open("./10_brute_force/words.txt", mode="r") as file:
        for i, line in enumerate(file, start=1):
            if word == line.strip():
                return f"Common match: {word} (#{i})"


def brute_force(word: str, length: int, /, digits: bool = False, symbols: bool = False):
    """
    Performs brute force on finding a word.

    By default, only lowercase ASCII letters are used.
    If 'digits' is True, digits (0-9) are included.
    If 'symbols' is True, punctuation symbols are included.
    """
    allowed_chars: str = string.ascii_lowercase

    if digits:
        allowed_chars += string.digits
    if symbols:
        allowed_chars += string.punctuation

    attempts: int = 0
    for guess in itertools.product(allowed_chars, repeat=length):
        attempts += 1
        guessed = "".join(guess)

        if word == guessed:
            return f'"{word}" was cracked in {attempts:,} guesses.'

        # print(guess, attempts)  # Comment this out when you're not testing


def main() -> None:
    if len(sys.argv) > 1:
        password: str = sys.argv[1].lower()
    else:
        password = input("Enter the password to crack: ").lower()

    print("Searching...")

    start_time = time.perf_counter()

    if common_match := common_guess(password):
        print(common_match)
    else:
        if cracked := brute_force(
            password,
            len(password),
            digits=contains_digits(password),
            symbols=contains_symbols(password),
        ):
            print(cracked)
        else:
            print("There was no match...")

    end_time: float = time.perf_counter()
    print(f"Elapsed time: {round(end_time - start_time, 2)} secs")


if __name__ == "__main__":
    main()
