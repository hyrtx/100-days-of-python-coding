import os
import art
from random import choice

# Words List
fruits: list = ["apple", "banana", "strawberry", "tomato", "watermelon",
                "orange", "mango", "pear", "tangerine", "pineapple",
                "melon", "peach", "lemon", "papaya", "grape"]

# Game Config.
number_of_chances: int = 6 # Number of chances the player has
chosen_word: str = choice(fruits) # Word choice for the game
game_over: bool = False # Game over flag

display: list = []
for s in chosen_word:
    display.append("_")

print(art.logo)

while not game_over:
    print(art.stages[number_of_chances])
    print(" ".join(display))
    guess_letter: str = input("Choose a letter: ").lower()

    # If player choose a repeated word
    if guess_letter in display:
        os.system("cls")
        print("You've already pick up this letter, choose another")
    
    # If the player guessed a word
    elif guess_letter in chosen_word:
        os.system("cls")
        print("Nice! You got one letter right.")

        for s in range(len(chosen_word)):
            
            # Replacing the underscore with the guessed letter
            if guess_letter == chosen_word[s]:
                display[s] = guess_letter
            
        # If all the letters were discovered
        if "_" not in display:
            game_over = True
            os.system("cls")
            print("Congrats! You won the game!")
    
    # If the player missed the letter
    else:
        os.system("cls")
        print(f"We don't have the letter {guess_letter} in the word. You lost one chance")
        number_of_chances -= 1

        # If the number of chances reaches 0
        if number_of_chances == 0:
            game_over = True
            os.system("cls")
            print("Too bad, you don't have any more chances =(\nTry again another time.")
