import os
from art import logo

def get_bidder_info():
    """
    Function to get name and bid from user
    """
    bidder = {}
    bidder["name"] = input("What is your name? ")

    while True:
        try:
            bidder["bid"] = int(input("What is your bid? $"))
            return bidder
        except ValueError:
            print("Please enter a valid number.")

def get_bid_flag():
    """
    Function to get bid trigger from user ("yes" or "no")
    """
    while True:
        bid_flag = input("Are there any other bidders? Type \"yes\" or \"no\". ").lower()
        if bid_flag in ["yes", "no"]:
            return bid_flag
        else:
            print("Invalid input. Please enter \"yes\" or \"no\".")

def get_bidders():
    """
    Function to collect information from multiple bidders
    """
    bidders_list = []

    while True:
        bidder = get_bidder_info()
        bidders_list.append(bidder)
        bid_flag = get_bid_flag()

        if bid_flag == "no":
            return bidders_list
        else:
            os.system("cls")

def auction():
    # Function to conduct the auction and determine the winner
    bidders_list = get_bidders()
    winner = ""
    higher_bid = 0

    for i in bidders_list:
        if i["bid"] > higher_bid:
            winner = i["name"]
            higher_bid = i["bid"]

    print(f"The winner is {winner} with a bid of ${higher_bid}")

# Display the logo and run the auction
print(logo)
auction()