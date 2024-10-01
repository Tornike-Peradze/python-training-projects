# Project 3 - Treasure Island:

print('Welcome to the treasure Island.')
print('Your mission is to find the treasure.')
choice_direction = input("You're at a cross road. Where do you want to go? \n   Type left or right \n ")
if choice_direction.lower() == "left":
    swim_or_wait_choice = input("You've come to a lake. There is an island in the middle of the lake. \n"
                                "Type 'wait' to wait for a boat. Type 'swim' to swim across. \n ")
    if swim_or_wait_choice.lower() == 'wait':
        three_doors_choice = input("You arrive at the island unharmed. There is a house with 3 doors. \n"
                                   "One red, one yellow and one blue. Which colour do you choose? \n ")
        if three_doors_choice.lower() == 'red':
            print('Burned by fire. Game Over.')
        elif three_doors_choice.lower() == 'blue':
            print('Eaten by beasts. Game Over.')
        elif three_doors_choice.lower() == 'yellow':
            print('You Win!')
        else:
            print('Game Over.')
    else:
        print('Attacked by trout. Game Over.')
else:
    print('Fall into a hole. Game Over.')