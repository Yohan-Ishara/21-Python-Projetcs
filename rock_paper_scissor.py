import random

user_wins = 0
computer_wins = 0

options = ['rock', 'paper', 'scissors']

while True:
    user_input = input("Type Rock, Paper, Scissors or get quit type Q: ").lower()

    if user_input == 'q':
        break

    if user_input not in options:
        print("Please enter valid type.")
        continue

    random_number = random.randint(0, 2)
    computer_pick = options[random_number]

    if user_input == 'rock' and computer_pick == 'scissors':
        user_wins += 1
        print(f"You won ! computer picked {computer_pick}")

    elif user_input == 'paper' and computer_pick == 'rock':
        user_wins += 1
        print(f"You won ! computer picked {computer_pick}")

    elif user_input == 'scissors' and computer_pick == 'paper':
        user_wins += 1
        print(f'You won ! computer picked {computer_pick}')

    else:
        computer_wins += 1
        print("You loose ! computer picked", computer_pick)

print("Goo day to you")
print("Computer won ", computer_wins, "times")
print("User won ", user_wins, "times")
