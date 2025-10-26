print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You're at the cross road. Where do you want to go?")
corss_road_input = input('''\t Type "left" or "right"\n''')
if (corss_road_input == "left"):
    print("You've come to the lake. There is an island in the middle of the lake.")
    lake_input = input('''\t Type "wait" to wait for a boat. Type "swim" to swim across.\n''')
    if (lake_input == "wait"):
        print("You arrive at the island unharmed. There is a house with 3 doors .")
        house_input = input("\t one red, one yellow and one blue. Which colour do you choose?\n")
        if (house_input == "yellow"):
            print("You win!")
        else:
            print("Game Over!!! \n Try Again.")
    else:
        print("Game Over!!! \n Try Again.")
else:
    print("Game Over!!! \n Try Again.")
    

