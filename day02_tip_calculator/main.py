print("Welcome to Tip Calculator")

total_bill: float = float(input("What was the total bill? "))
tip_value: int = int(input("How much you want to tip? (10, 12 or 15) ")) / 100
number_of_people: int = int(input("How many people to share the bill? "))

tip_calculator: float = ((1 + tip_value) * total_bill) / number_of_people

print(f"The amount of the tip divided by {number_of_people} is ${tip_calculator}")