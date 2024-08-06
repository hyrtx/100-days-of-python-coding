from art import logo

print(logo)

print("Welcome to Treasure Island. Your mission is to find the treasure.")

direction_decision: str = input('You have arrived on the island, choose a direction: Left or Right ').strip().upper()

if direction_decision == 'LEFT':
  lake_decision: str = input('Very Well. You arrived at a lake. What are you going to do, Swim or Wait? ').strip().upper()

  if lake_decision == 'WAIT':
    door_decision: str = input('Good choice. You are faced with two doors, which one you choose: Red, Blue or Yellow? ').strip().upper()

    if door_decision == 'YELLOW':
      print('Congratulations. You win!')
    elif door_decision == 'RED':
      print('You were burned by fire. Game Over.')
    elif door_decision == 'BLUE':
      print('You were eaten by beasts. Game Over.')
    else:
      print('Game Over.')

  else:
    print('You have been attacked by a lake serpent. Game Over.')

else:
  print('You fell into a hole. Game Over.')