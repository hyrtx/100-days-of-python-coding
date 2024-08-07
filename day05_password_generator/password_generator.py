import random

# List with characters
letters: list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                 "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
                 "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
                 "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
numbers: list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols: list = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]


print("Welcome to the PyPassword Generator!")

# User input
number_of_letters: int = int(input(f"How many letters would you like in your password?\n"))
number_of_numbers: int = int(input(f"How many numbers would you like?\n"))
number_of_symbols: int = int(input(f"How many symbols would you like?\n"))

# Creation of a list with the characters in a quantity specified by the user
password_list: list = []

for i in range(1, number_of_letters + 1):
    password_list.append(random.choice(letters))

for i in range(1, number_of_numbers + 1):
    password_list.append(random.choice(numbers))

for i in range(1, number_of_symbols + 1):
    password_list.append(random.choice(symbols))

# Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
random.shuffle(password_list)
password: str = ''.join(password_list)

# Impression of the password
print(f"Your password is: {password}")
