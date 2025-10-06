from random import randint
from sys import exit

while True:
    user_input = input("How many dice would you like to roll? ")
    try:
        total_dice = int(user_input)
    except ValueError:
        if user_input == "exit":
            print("Thanks for playing!")
            exit()
        continue
    dices: list[int] = []
    for _ in range(total_dice):
        dices.append(randint(1, 6))
    print(*dices, sep=", ")
