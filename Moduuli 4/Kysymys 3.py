number = input("Enter a number (or press Enter to quit): ")

little = None
big = None

while number != "":
    luku = float(number)

    if little is None or luku < little:
        little = luku

    if big is None or luku > big:
        big = luku

    number = input("Enter a number (or press Enter to quit): ")

if little is not None:
    print(f"Smallest number: {little:.1f}")
    print(f"Largest number: {big:.1f}")