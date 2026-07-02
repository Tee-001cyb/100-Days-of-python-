while True:  
    bill = float(input("How much is the bill:"))
    tip = (input("how many percent are you tipping (10, 20, 30, or 'n': "))
    if tip == "n":
        Tip = 0
        Print("No tip added")
    else:
        tip = float(tip)
          Tip = (bill /100 * tip)
    total_amount = bill + Tip
    print(f"Here is your total bill including tips, {total_amount}")
    people = float(input("how many people are spilting the bills split to?: "))
    payment_per_person = total_amount / people
    print(f"Here is the payment for each person {payment_per_person}")
    instruction = input("do you want to exit press 'y',(or 'n' to continue) ")
    if instruction == 'y':
         print("Calculation done")
