from art import logo
from time import sleep
from machine import MENU

resources: dict = {
    'water': 300,
    'milk': 200,
    'coffee': 100
}

profit: float = 0

def get_product_cost(product_name: str) -> float:
    '''Get the cost price of a product'''
    product_cost: float = MENU[product_name]['cost']
    return product_cost

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
    ingredients: dict = MENU[product_choice]['ingredients']

    for item in ingredients:
        if ingredients[item] > resources[item]:
            print(f"Sorry, there aren't enough {item} to prepare a {coffee_choice}")
            return False
        else:
            return True
        
def process_coins() -> float:
    '''Process the payment in coins made by the client'''
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
        
    payment = sum(coins.values())

    return payment

def check_payment(payment: float, product_choice: str) -> bool:
    '''Check if the payment made by the client is correct'''
    product_price: float = get_product_cost(product_choice)
    change: float = 0.0

    if payment == product_price:
        return True
    elif payment > product_price:
        change = payment - product_price
        print(f"Here is ${round(change, 2)} dollars in change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(product_choice: str) -> None:
    '''Make the coffee and deduct the ingredients used from resources. 
    There is no return the function'''
    ingredients: dict = MENU[product_choice]['ingredients']

    for item in ingredients:
        resources[item] -= ingredients[item]
    
    print(f"Here's your {product_choice}. Enjoy!")

while True:
    # Prompt user by asking “What would you like? (espresso/latte/cappuccino)
    print(logo)
    coffee_choice: str = input("What would you like? (espresso/latte/cappuccino): ").strip().lower()

    # Turning off option for maintenance
    if coffee_choice == 'off':
        print("Turning off the machine...")
        break

    # Print report
    elif coffee_choice == 'report':
        get_report()
        sleep(5)
        continue
        
    # Check if resources are sufficient
    elif coffee_choice in MENU:
        
        # Convert the coins to dollars
        if check_resources(coffee_choice):
            coffee_payment = process_coins()
            
            # Check if the transacion was successful
            if check_payment(coffee_payment, coffee_choice):
                profit += get_product_cost(coffee_choice)
                make_coffee(coffee_choice)
                sleep(3)
                continue
            else:
                sleep(3)
                continue
        
        else:
            sleep(3)
            continue
        
    else:
        print("We don't have this option. Try one of our coffees.")
        sleep(3)