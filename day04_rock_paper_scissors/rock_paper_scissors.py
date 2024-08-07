import art
from random import choice

print(art.logo)

# List with the game choices where 0 = Rock, 1 = Paper and 2 = Scissor.
game_choices: list = [0, 1, 2]
game_images: list = [art.rock_image, art.paper_image, art.scissor_image]
choice_name: list = ["rock", "paper", "scissor"]

# Computer choice
computer_choice: int = choice(game_choices)

# Player choice
valid_choice: bool = False

while not valid_choice:
    player_choice: int = int(input("Select one option: 0 = Rock, 1 = Paper and 2 = Scissor "))
    
    if player_choice in game_choices:
        valid_choice = True
    else:
        print("Please, select a valid option")

# Match
print(f"You choose {choice_name[player_choice].capitalize()}\n")
print(game_images[player_choice])

print(f"\n\nComputer choose {choice_name[computer_choice].capitalize()}\n")
print(f"{game_images[computer_choice]}\n")

# Result if player chooses rock
if player_choice == 0:

  if computer_choice == 0:
    print("Draw")
  elif computer_choice == 1:
    print("You lose. Try Again!")
  elif computer_choice == 2:
    print("Congratulations! You won")

# Result if player chooses paper
elif player_choice == 1:

  if computer_choice == 0:
    print("Congratulations! You won")
  elif computer_choice == 1:
    print("Draw")
  elif computer_choice == 2:
    print("You lose. Try Again!")

# Result if player chooses scissors
elif player_choice == 2:

  if computer_choice == 0:
    print("You lose. Try Again!")
  elif computer_choice == 1:
    print("Congratulations! You won")
  elif computer_choice == 2:
    print("Draw")