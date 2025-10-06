def check_password(password: str):
    """Checks whether a password is in the 1,00,000 most common passwords."""

    with open("./09_common_password_checker/passwords.txt", mode="r") as file:
        for i, line in enumerate(file, start=1):
            if password == line.strip():
                print(f"{password}: ❌ (#{i})")
                return

    print(f"{password}: ✅ (Unique)")


def main() -> None:
    user_password: str = input("Enter a password: ")
    check_password(password=user_password)


if __name__ == "__main__":
    main()
