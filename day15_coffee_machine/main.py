import art
import machine

resources: dict = {
    'water': 300,
    'milk': 200,
    'coffee': 100
}

profit: float = 0

def get_report() -> None:
    '''Function to print the machine report'''
    unit: str = ""

    for k, v in resources.items():
        if k == 'coffee':
            unit = 'g'
        else:
            unit = 'ml'
        print(f"{k}: {v}{unit}")

    print(f"Profit: ${profit}")

def check_resources(product_choice: str) -> bool:
    '''Check if the machine has the resources to process the coffee'''
    ingredients: dict = machine.MENU[product_choice]['ingredients']

    for item in ingredients:
        if ingredients[item] > resources[item]:
            print(f"Sorry, there aren't enough {item} to prepare a {coffee_choice}")
            return False
        else:
            return True
        
def process_coins():
    coins: dict = {}
    payment: float = 0

    print("Please, insert coins")

    while True:
        try:
            coins['quarter'] = int(input("How many quarters? ")) * 0.25 # Value of quarter
            coins['dime'] = int(input("How many dimes? ")) * 0.10 # Value of dime
            coins['nickel'] = int(input("How many nickes? ")) * 0.05 # Value of nickel
            coins['penny'] = int(input("How many pennies? ")) * 0.01 # Value of penny
            break
        except ValueError:
            print("Please, insert coins on the machine")
            continue
        except Exception as e:
            print(e)
            print(type(e))
        
    payment = sum(coins.values)

    return payment

while True:
    # Prompt user by asking “What would you like? (espresso/latte/cappuccino)
    coffee_choice: str = input("What would you like? (espresso/latte/cappuccino): ")

    # Turning off option
    if coffee_choice == 'off':
        print("Turning off the machine...")

    # Print report
    elif coffee_choice == 'report':
        get_report()
        break
        
    # Check resources sufficient
    elif coffee_choice in machine.MENU:
        
        if check_resources(coffee_choice):
            coffee_payment = process_coins()
            print(coffee_payment)
        
        else:
            print("We don't have this option. Try one of our coffees.")
            continue