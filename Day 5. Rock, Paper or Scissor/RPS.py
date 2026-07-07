import random

def computer():
    option = ["Rock", "Paper", "Scissors"]

    while True:
         
        instructions = {
          "rock": "scissors",
          "paper": "rock",
          "scissors": "paper"
          }

        print("Pick one")
        print("Rock")
        print("Paper")
        print("Scissors")

        computer_choice = random.choice(option).lower()

        options = input("Rock, Paper or Scissors: ").lower()
        if options == computer_choice:
            print(f"Computer: {computer_choice}")
            print("IT'S A TIE")
            exit_game = input("Would you like to continue the game 'y'/ 'n': ").lower()
            if exit_game == "n":
               break

        elif instructions[options] == computer_choice:
            print(f"Computer: {computer_choice}")
            print("YOU WON!!")
            exit_game = input("Would you like to continue the game 'y'/ 'n': ").lower()
            if exit_game == "n":
               break

        else:
            print(f"Computer: {computer_choice}")
            print("YOU LOSE")
            exit_game = input("Would you like to continue the game 'y'/ 'n': ").lower()
            if exit_game == "n":
               break

computer()