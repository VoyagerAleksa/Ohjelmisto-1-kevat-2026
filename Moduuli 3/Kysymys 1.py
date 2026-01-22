pituus = float(input("Enter the length of the zander in centimeters: "))

if pituus < 42:
    puuttuvat_sentit = round(42 - pituus, 1)
    print("The zander does not meet the size limit.")
    print("Please release the fish back into the lake.")
    print(f"The fish was {puuttuvat_sentit} centimeters below the size limit.")

if pituus >= 42:
    print("The zander meets the size limit.")