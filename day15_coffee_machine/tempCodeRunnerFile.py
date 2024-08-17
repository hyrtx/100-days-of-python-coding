import art
import machine

resources: dict = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}

money: float = 0

def get_report():
    unit: str = ""

    for k, v in resources.items():

        if k == "coffee":
            unit = "g"
        else:
            unit = "ml"

        print(f"{k}: {v}{unit}")
    
    print(f"Money: ${money}")


while True:
    # Prompt user by asking “What would you like? (espresso/latte/cappuccino)
    choice: str = input("What would you like? (espresso/latte/cappuccino): ")

    # Print report
    if choice == "report":
        get_report()
        break
        