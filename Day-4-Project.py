import random

user_input = (input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissor\nuser choice: ")).lower()
game_menu = ["rock", "paper", "scissor"]
computer_choice = random.choice(game_menu)
print("computer choice: ",computer_choice)

if (user_input == "rock"):
    if (computer_choice == "paper"):
         print("Computer Won!!!")
    if (computer_choice == "scissor"):
         print("user Won!!!")
if (user_input == "paper"):
    if (computer_choice == "scissor"):
         print("Computer Won!!!")
    if (computer_choice == "rock"):
         print("user Won!!!")
if (user_input == "scissor"):
    if (computer_choice == "rock"):
         print("Computer Won!!!")
    if (computer_choice == "paper"):
         print("user Won!!!")
if (user_input == computer_choice):
     print("It's a draw match")