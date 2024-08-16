import art
import os
from random import choice
from instagram_accounts import instagram_accounts

def get_contestant() -> dict:
    """Randomly pick one instagram account from the account dictionary and return another dictionary."""
    contestant: dict = choice(list(instagram_accounts.items()))
    return contestant[1]

def compare_contestants(cont_a: dict, cont_b: dict) -> str:
    """Compare the two contestants and returns the letter to the one with more followers."""
    if cont_a['followers_millions'] > cont_b['followers_millions']:
        return "a"
    elif cont_a['followers_millions'] < cont_b['followers_millions']:
        return "b"
    else:
        return "even"

def get_user_choice():
    """Get the guess letter from user"""
    while True:
        try:
            user_choice: str = input("Who has more followers? Select 'A' or 'B': ").strip().lower()
        except ValueError:
            print("Select an option between A or B.")
            continue
        except Exception as e:
            print(e)
            print(type(e))

        if user_choice in ["a", "b"]:
            return user_choice
        else:
            print("Select an option between A or B.")
            continue

score: int = 0
contestant_a: dict = get_contestant()

print(art.logo)
print("Welcome to the Higher Lower Game")

while True:

    while True:
        contestant_b: dict = get_contestant()

        if contestant_b != contestant_a:
            break

    print(f"Your Score: {score}")

    # Choose the contestants
    print(f"Pick A: {contestant_a['name']}, a {contestant_a['description']}, from {contestant_a['country']}")
    print(art.vs_logo)
    print(f"Pick B: {contestant_b['name']}, a {contestant_b['description']}, from {contestant_b['country']}")

    # Make the user choose between the two contestants
    correct_answer: str = compare_contestants(contestant_a, contestant_b)
    user_choice: str = get_user_choice()

    # Add the score if player choosed right. Otherwise, gameover

    if correct_answer == user_choice:
        score += 1
        print(f"Nice, you guessed right!")
        os.system("cls")
        print(art.logo)
        
        if correct_answer == "b":
            contestant_a = contestant_b

    else:
        os.system("cls")
        print(art.logo)
        print(f"You missed. Final Score: {score}")
        break