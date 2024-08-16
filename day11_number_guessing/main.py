from art import logo
from random import randint

# Global variables
EASY_ATTEMPTS: int = 10
HARD_ATTEMPTS: int = 5

def difficulty() -> int:
    """Function to get the number of attempts according to the choosen difficulty."""
    while True:
        
        try:
            difficulty: str = input("Type 'easy' or 'hard': ").strip().lower()
        except ValueError:
            print('Please, choose the difficulty given.')
            continue
        except Exception as e:
            print(e)
            print(type(e))
            break

        if difficulty == 'easy':
            return EASY_ATTEMPTS
        elif difficulty == 'hard':
            return HARD_ATTEMPTS
        else:
            print("Print a valid difficulty")

def guess_number() -> int:
    """Guess and valid a number choosed by the player."""
    while True:

        try:
            number: int = int(input("Guess a number between 1 and 100: "))
        except ValueError:
            print("Choose a number.")
            continue
        except Exception as e:
            print(e)
            print(type(e))
            break

        if 1 <= number <= 100:
            return number
        else:
            print("Please, choose a number from the given range.")

# Game Script
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

correct_number: int = randint(1, 100)
attempts: int = difficulty()

while True:
    print(f"You have {attempts} attempts.")
    guessed_number: int = guess_number()

    if guessed_number == correct_number:
        print("Nice, you won!")
        break
    else:
        attempts -= 1

        if attempts == 0:
            print(f"Too bad, the correct number is {correct_number}.")
            print("Try again.")
            break
        elif guessed_number > correct_number:
            print("Too high.")
            print("Try again.")
        else:
            print("Too low.")
            print("Try again.")