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

dealer_hand: list = get_dealer_hand()
player_hand: list = []

for i in range(0, 2):
    card: int = get_card()

    if card == 11 and sum(player_hand) > 10:
        player_hand.append(1)
    else:
        player_hand.append(card)

while sum(player_hand) < 21:
    print(f"    Your cards: {player_hand}, current score: {sum(player_hand)}")
    print(f"    Dealer's first card: {dealer_hand[0]}")
    
    draw_flag: str = input("Type 'y' to get another card, type 'n' to pass: ").strip().lower()
    
    if draw_flag == "y":

        if card == 11 and sum(player_hand) > 10:
            player_hand.append(1)
        else:
            player_hand.append(card)
    
    else:
        break

if sum(player_hand) > 21:
    print(f"   Your final hand: {player_hand}, total score: {sum(player_hand)}")
    print(f"   Dealer's final hand: [{dealer_hand[0]}], total score: {dealer_hand[0]}")
    print("You busted! Dealer Wins")

elif sum(dealer_hand) > 21:
    print(f"   Your final hand: {player_hand}, total score: {sum(player_hand)}")
    print(f"   Dealer's final hand: {dealer_hand}, total score: {sum(dealer_hand)}")
    print("You Won! Congratulations!")

elif sum(player_hand) > sum(dealer_hand):
    print(f"   Your final hand: {player_hand}, total score: {sum(player_hand)}")
    print(f"   Dealer's final hand: {dealer_hand}, total score: {sum(dealer_hand)}")
    print("You Won! Congratulations!")

else:
    print(f"   Your final hand: {player_hand}, total score: {sum(player_hand)}")
    print(f"   Dealer's final hand: {dealer_hand}, total score: {sum(dealer_hand)}")
    print("Dealer wins! Congratulations!")