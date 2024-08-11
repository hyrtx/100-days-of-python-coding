from art import logo
from random import choice

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

def get_dealer_hand():
    """Draw the dealer cards from the deck"""
    dealer_hand: list = []
    card: int = get_card()

    while sum(dealer_hand) < 18:
        if card == 11 and sum(dealer_hand) > 10:
            dealer_hand.append(1)
        else:    
            dealer_hand.append(card)
    return dealer_hand

def get_player_card():
    """Draw one card for the player"""
    card: int = get_card()

    if card == 11 and sum(player_hand) > 10:
        return 1
    else:
        return card

def result(player_hand: list, dealer_hand: list) -> str:
    """Determine the game result"""
    if sum(player_hand) > 21:
        return "You busted! Dealer Wins"
    elif sum(dealer_hand) > 21 or sum(player_hand) > sum(dealer_hand):
        return "You Won! Congratulations!"
    else:
        return "Dealer wins! Congratulations!"


dealer_hand: list = get_dealer_hand()
player_hand: list = []

# Drawing the first two player's cards
for i in range(0, 2):
    player_hand.append(get_card)

# Giving the player the choice to draw another card
while sum(player_hand) < 21:
    print(f"    Your cards: {player_hand}, current score: {sum(player_hand)}")
    print(f"    Dealer's first card: {dealer_hand[0]}")
    
    draw_flag: str = input("Type 'y' to get another card, type 'n' to pass: ").strip().lower()
    
    if draw_flag == "y":
        card = get_player_card()
        if card == 11 and sum(player_hand) > 10:
            player_hand.append(1)
        else:
            player_hand.append(card)
    else:
        break

print(f"   Your final hand: {player_hand}, total score: {sum(player_hand)}")
print(f"   Dealer's final hand: {dealer_hand}, total score: {sum(dealer_hand)}")
print(result)