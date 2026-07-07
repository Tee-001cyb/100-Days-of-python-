def Treasure_hunt():
   while  True:
     print("Welcome to treasure Island, your mission is to find the treasure")
     Choice1 = input("You're at a cross road, where do you want to go? Type 'left' or 'right': ").lower()
     if Choice1 == "right":
      print("You just fell into a hole. Game Over.")
      Restart = input("Would you like to restart the game? 'y' or 'n': ").lower()
      if Restart == "y":
         Treasure_hunt()

     else:
      choice2 = input("You have to cross a leak to get to the Treasure, you have two options, 'wait' for a boat or 'swim' across: ").lower()
      if choice2 == "swim":
         print("Oops!!, You were attacked by a trout. Game Over.")
         Restart = input("Would you like to restart the game? 'y' or 'n':  ").lower()
         if Restart == "y":
            Treasure_hunt()
      else:
         choice3 = input("congrant, You have reached the island, you have three doors to choose from, 'red', 'blue' or 'yellow'. Which one do you choose?: ").lower()
         if choice3 == "red":
            print("You were burned by fire. Game Over.")
            Restart = input("Would you like to restart the game? 'y' or 'n': ").lower()
            if Restart == "y":
               Treasure_hunt()
         elif choice3 == "blue":
            print("Oop!!!, You were eaten by beasts. Game Over.")
            Restart = input("Would you like to restart the game? 'y' or 'n': ").lower()
            if Restart == "y":
               Treasure_hunt()
         elif choice3 == "yellow":
            print("Congratulations! You found the treasure. You Win!")
            Restart = input("Would you like to play again? 'y' or 'n':").lower()
            if Restart == "y":
               Treasure_hunt()
            else:
               print("Thank you for playing. Goodbye!")
               break
         else:
            print("Game Over.")
     

Treasure_hunt()