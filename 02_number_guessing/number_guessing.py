from random import randint

lower_number, higher_number = 1, 10
random_number = randint(1, 10)
print(f"Guess the number in the range from {lower_number} to {higher_number}.")


while True:
    try:
        user_guess = int(input("Guess: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if user_guess > random_number:
        print("The number is lower")
    elif user_guess < random_number:
        print("The number is higher")
    else:
        print("You guessed it!")
        break
