import random

def roll_dice():
    dice_number = random.randint(1, 6)
    return dice_number
print(" This is dice rolling example")

while 1:
    Selection = input("do you want to roll a dice (y/n): ")
    if 'y' in Selection.lower():
        print("Rolling Dice...")
        number = roll_dice()
        print("Dice has the number: ", number)
    elif 'n' in Selection.lower():
        'n' in Selection.lower()
        print("Exiting...")
        break
    else:
        print("Invalid input... please try again")