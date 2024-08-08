from art import logo
from typing import Callable

OperatorFunction = Callable[[float, float], float]

def add(a: float, b: float) -> float:
    return a + b

def subtract(a: float, b: float) -> float:
    return a - b

def multiply(a: float, b: float) -> float:
    return a * b

def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

operators: dict = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def get_number(prompt: str) -> float:
    """It receives a number from the user and manipulates it from string to float and handles possible errors."""
    while True:
        try:
            return float(input(prompt).replace(",", "."))
        except ValueError:
            print("Please, enter a valid number.")
        except Exception as e:
            print(e)
            print(type(e))

def get_operator() -> OperatorFunction:
    while True:
        operator: str = input("Select one operator: ['+', '-', '*', '/'] ").strip()
        if operator in operators:
            return operator
        print("Choose a valid operator.")

print(logo)
print("Welcome to the calculator")

number_1: float = get_number("Select the first number: ")
operator: OperatorFunction = get_operator()
number_2: float = get_number("Select the second number: ")

result: float = operators[operator](number_1, number_2)

print(f"The result is: {result}")