from art import logo
from random import choice

print(logo)

def get_card():
    cards: dict = {
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "10": 10,
        "Jack": 10,
        "Queen": 10,
        "King": 10,
        "Ace": 11
        }
    
    return choice(list(cards.values()))