import os
from art import logo

def ceasar(direction_option: str, plain_text: str, shift_amount: int):
    alphabet: list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", 
                "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", 
                "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", 
                "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    ceasar_word: str = ""
    
    # Shift amount validation to prevents index error.
    if shift_amount > 26:
        shift_amount %= 26

    # Scenario in which encode option is selected
    if direction_option == "encode":
        for _ in range(0, len(plain_text)):
            if plain_text[_] in alphabet: # If letter isn"t in the list, repeat the character
                ceasar_word += alphabet[alphabet.index(plain_text[_]) + shift_amount]
            else:
                ceasar_word += plain_text[_]
        print(f"The encoded text is '{ceasar_word}'")

    # Scenario in which decode option is selected
    elif direction_option == "decode":
        for _ in range(0, len(plain_text)):
            if plain_text[_] in alphabet: # If letter isn"t in the list, repeat the character
                ceasar_word += alphabet[alphabet.index(plain_text[_]) - shift_amount]
            else:
                ceasar_word += plain_text[_]
        print(f"The decoded text is \"{ceasar_word}\"")

    # Scenario in which the encoding or decoding options are not selected
    else:
        print("This option is not available.")

while True:
    os.system("cls")
    print(logo)
    
    direction: str = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text: str = input("Type your message:\n").lower()
    shift: int = int(input("Type the shift number:\n"))
    
    ceasar(direction_option= direction, plain_text= text, shift_amount= shift)
    
    # Restart option.
    restart: str = input("Type 'yes' if you want to go again. Otherwise type 'no': ").lower()
    if restart != "yes":
        print("Goodbye")
        break
