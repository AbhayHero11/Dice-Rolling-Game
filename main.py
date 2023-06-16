import random

while True:
    print("\n--- Dice Rolling Simulator ---")
    print("Press Enter to roll the dice or X to exit.")
    choice = input("Your choice: ")

    if choice.lower() == "x":
        print("Thank you for using the Dice Rolling Simulator. Goodbye!")
        break

    dice_roll = random.randint(1, 6)
    print(f"The dice rolled: {dice_roll}")