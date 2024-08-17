import art
import machine

resources: dict = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}

money: float = 0

def get_report() -> None:
    unit: str = ""

    for k, v in resources.items():
        if k == "coffee":
            unit = "g"
        else:
            unit = "ml"
        print(f"{k}: {v}{unit}")

    print(f"Money: ${money}")

def check_resources(product_choice: str):
    ingredients: dict = machine.MENU[product_choice]['ingredients']

    for item in ingredients:
        if ingredients[item] > resources[item]:
            print(f"Sorry, there aren't enough {item} to prepare a {coffee_choice}")
            return False
        else:
            return True

while True:
    # Prompt user by asking “What would you like? (espresso/latte/cappuccino)
    coffee_choice: str = input("What would you like? (espresso/latte/cappuccino): ")

    # Turning off option
    if coffee_choice == "off":
        print("Turning off the machine...")

    # Print report
    elif coffee_choice == "report":
        get_report()
        break
        
# Check resources sufficient
    elif coffee_choice in machine.MENU:
        check_resources(coffee_choice)
