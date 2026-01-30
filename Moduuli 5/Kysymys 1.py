import random

dices_enter = int(input("How many dice to roll: "))
results = []

for _ in range(dices_enter):
    results.append (random.randint(1,6))

summa_dices = sum(results)


print(f"Sum of the dice: {summa_dices} ")