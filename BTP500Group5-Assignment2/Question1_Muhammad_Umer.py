# Completed by: Muhammad Umer – Group #5
# Question 1: Snakes and Ladders Game

import random

# Function to roll dice
def roll_dice():
    return random.randint(1, 6)

# Board (Snakes and Ladders using dictionary)
board = {
    3: 22,   # Ladder
    5: 8,
    11: 26,
    20: 29,
    27: 1,   # Snake
    21: 9,
    17: 4,
    19: 7
}

# Player positions
players = {
    "Player 1": 0,
    "Player 2": 0
}

# Function to move player
def move_player(player):
    dice = roll_dice()
    print(f"{player} rolled a {dice}")

    # Move forward
    players[player] += dice

    # Check if player exceeds 30
    if players[player] > 30:
        players[player] -= dice
        print(f"{player} needs exact number to reach 30!")

    # Check snakes or ladders
    if players[player] in board:
        old_pos = players[player]
        players[player] = board[players[player]]

        if old_pos < players[player]:
            print(f"{player} climbed a ladder from {old_pos} to {players[player]}!")
        else:
            print(f"{player} got bitten by a snake from {old_pos} to {players[player]}!")

    print(f"{player} is now at position {players[player]}\n")


# Game Loop
def play_game():
    print("Welcome to Snakes and Ladders (First to reach 30 wins!)\n")

    turn = 0
    player_names = list(players.keys())

    while True:
        current_player = player_names[turn % 2]

        input(f"{current_player}'s turn (Press Enter to roll dice).")
        move_player(current_player)

        # Check winner
        if players[current_player] == 30:
            print(f"{current_player} WINS THE GAME!")
            break

        turn += 1


# Run game
play_game()