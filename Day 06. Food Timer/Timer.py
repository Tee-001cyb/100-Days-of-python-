import time

FOOD_TIME = {"Noodles": 300,
             "Hard boiled egg": 600,
             "Fried egg": 240,
             "Rice": 1200,
             "Spaghetti": 600,
             "Fish": 900,
            "Chicken breast": 1500,
            "Beans": 5400,
            "Boiled potatoes": 1200}
def countdown(setting):
     for x in reversed(range(0, setting)):
            seconds = x % 60
            minutes = int(x / 60) % 60
            hours = int(x / 3600)
            print(f"{hours:02d}:{minutes:02d}:{seconds:02d}", end="\r")
  #The \r (carriage return) moves the cursor back to the beginning of the current line so the next time is written over the previous one.
            time.sleep(1)

def digital_time():
    print("--------------------FOOD TIMER--------------------")
    print("Select a food item from the list below to set the timer")
    
    for food, seconds in FOOD_TIME.items():
     print(f"{food:<20} : {seconds:>20} seconds")
    
    food = input("Choose a food: ").title()
    if food in FOOD_TIME:
        print("Timer started")
        setting =(FOOD_TIME[food])
        print(f"Cooking time for {food} is {setting} seconds")
        countdown(setting)
        print("Food is ready!")
    else:
        print("Invalid food item, add it to the list and try again")
        food = input("Enter food name: ").title()
        seconds = int(input("Enter cooking time in seconds: "))
        FOOD_TIME[food] = seconds
        for food, seconds in FOOD_TIME.items():
            print(f"{food:<20} : {seconds:>20} seconds")
        food = input("Choose a food: ").title()
        print(f"Cooking time for {food} is {seconds} seconds")
        countdown(seconds)
        print("Food is ready!")
        
digital_time()
