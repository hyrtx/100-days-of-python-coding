from art import logo

def calculator(first_number: float, second_number: float, operator: str) -> float:
    """Performs mathematical calculations of addition, subtraction, multiplication and division."""
    if operator == "+":
        return first_number + second_number
    elif operator == "-":
        return first_number - second_number
    elif operator == "*":
        return first_number * second_number
    elif operator == "/":
        return first_number / second_number
    else:
        return None
    
print(logo)
print("Welcome to the calculator")

number_1: float = float(input("Select the first number: ").replace(",", "."))

while True:
    operator_list: list = ["+", "-", "*", "/"]
    operator: str = input("Select one operator: ['+', '-', '*', '/'] ").strip()

    if operator in operator_list:
        break
    else:
        print("Please, choose a valid operator.")

number_2 = float(input("Select the second number: ").replace(",", "."))
result: float = calculator(first_number= number_1, second_number= number_2, operator= operator)

print(f"The result is: {result}")