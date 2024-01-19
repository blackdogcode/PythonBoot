import random
import emoji

winning_condition = [
    # 0 - Rock, 1 - Paper, 2 - Scissors
    # Rock
    [
        "Draw", "Lose", "Win"
    ],
    # Paper
    [
        "Win", "Draw", "Lose"
    ],
    # Scissors
    [
        "Lose", "Win", "Draw"
    ]
]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))
computer_choice = random.randint(0, 2)

hand_icon = [emoji.rock, emoji.paper, emoji.scissors]
print(f"{hand_icon[computer_choice]}")
print("Computer chose:")
print(f"{hand_icon[user_choice]}")

result = winning_condition[user_choice][computer_choice]
print(f"You {result}")

