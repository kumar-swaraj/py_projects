import secrets
import string


def contains_uppercase(password: str) -> bool:
    """Check if a password contains uppercase characters."""
    return any(char.isupper() for char in password)


def contains_symbols(password: str) -> bool:
    """Check if a password contains symbols."""
    return any(char in string.punctuation for char in password)


def generate_password(length: int, symbols: bool, uppercase: bool) -> str:
    """
    Generates a random password of specified length with optional symbols and uppercase letters.

    Args:
        length (int): The desired length of the password.
        symbols (bool): If True, include punctuation symbols in the password.
        uppercase (bool): If True, include uppercase letters in the password.

    Returns:
        str: The generated random password.
    """
    allowed_characters: str = string.ascii_lowercase + string.digits

    if symbols:
        allowed_characters += string.punctuation
    if uppercase:
        allowed_characters += string.ascii_uppercase

    combination_length: int = len(allowed_characters)

    password_chars: list[str] = []

    for _ in range(length):
        password_chars.append(allowed_characters[secrets.randbelow(combination_length)])

    return "".join(password_chars)


if __name__ == "__main__":
    # Generate 5 random passwords
    for i in range(1, 6):
        password = generate_password(30, True, True)
        specs = f"Uppercase: {contains_uppercase(password)}, Symbols: {contains_symbols(password)}"

        print(f"{i} -> {password} ({specs})")
