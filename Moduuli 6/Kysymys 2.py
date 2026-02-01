import random
def roll_dice(side):
    return random.randint(1,side)
sides_enter = int(input("Enter the number of sides: "))

while True:
    result = roll_dice(sides_enter)
    print(result)
    if result == sides_enter:
        break
