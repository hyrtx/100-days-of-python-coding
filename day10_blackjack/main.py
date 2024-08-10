from art import logo
from random import choice

print(logo)

def get_card():
    """Function to get a card from the deck"""
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

player_hand: list = []

def get_dealer_hand():
    """Draw the dealer cards from the deck"""
    dealer_hand: list = []
    card = get_card()

    while sum(dealer_hand) < 18:

        if card == 11 and sum(dealer_hand) > 10:
            dealer_hand.append(1)
        else:    
            dealer_hand.append(card)
    
    return dealer_hand

print(get_dealer_hand())