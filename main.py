import random

while True:
    print("\n---Dice Rolling Sim---")
    print("Press Enter to roll dice or X to exit.")
    choice = input("Your Choice: ")

    if choice.lower() == "x":
        print("Thank you for using the Dice Rolling Sim. Goodbye!!")
        break

    dice_roll = random.randint(1,6)
    print(f"The dice rolled: {dice_roll}")