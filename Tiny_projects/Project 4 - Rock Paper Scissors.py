# Project 4 - Rock Paper Scissors

import random

print('Welcome to the Rock Paper Scissors game!')

rock_var = '''
    
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

'''

paper_var = '''

    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

'''

scissors_var = '''

    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''

list_of_signatures = [rock_var, paper_var, scissors_var]

computer_chosen_signature = random.randint(0, 2)

user_input_signature = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n "))

if user_input_signature == 0 and computer_chosen_signature == 1:
    print(f'User chose: \n {list_of_signatures[0]} \n computer chose: {list_of_signatures[1]} \n Computer Wins!')
elif user_input_signature == 0 and computer_chosen_signature == 2:
    print(f'User chose: \n {list_of_signatures[0]} \n computer chose: {list_of_signatures[2]} \n User Wins!')
elif user_input_signature == 1 and  computer_chosen_signature == 0:
    print(f'User chose: \n {list_of_signatures[1]} \n computer chose: {list_of_signatures[0]} \n User Wins!')
elif user_input_signature == 1 and computer_chosen_signature == 2:
    print(f'User chose: \n {list_of_signatures[1]} \n computer chose: {list_of_signatures[2]} \n Computer Wins!')
elif user_input_signature == 2 and computer_chosen_signature == 0:
    print(f'User chose: \n {list_of_signatures[2]} \n computer chose: {list_of_signatures[0]} \n Computer Wins!')
elif user_input_signature == 2 and computer_chosen_signature == 1:
    print(f'User chose: \n {list_of_signatures[2]} \n computer chose: {list_of_signatures[1]} \n User Wins!')
elif user_input_signature == 0 and computer_chosen_signature == 0:
    print(f'User chose: \n {list_of_signatures[0]} \n computer chose: {list_of_signatures[0]} \n It is a draw!')
elif user_input_signature == 1 and computer_chosen_signature == 1:
    print(f'User chose: \n {list_of_signatures[1]} \n computer chose: {list_of_signatures[1]} \n It is a draw!')
elif user_input_signature == 2 and computer_chosen_signature == 2:
    print(f'User chose: \n {list_of_signatures[2]} \n computer chose: {list_of_signatures[2]} \n It is a draw!')
else:
    print('You entered invalid value, please try again!')