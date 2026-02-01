def gallons_to_liters (gallons_float):
    liters_float = gallons_float * 3.785
    return liters_float

while True:
    gallons_str = input("Enter a volume in American gallons (negative value to quit): ")
    gallons_float = float(gallons_str)
    if gallons_float < 0:
        break
    else:
        liters_float = gallons_to_liters(gallons_float)
        print(f"{gallons_float:.1f} American gallons is {liters_float:.2f} liters.")

print("Program finished.\n")
