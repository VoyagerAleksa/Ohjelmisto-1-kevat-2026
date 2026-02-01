import math
def calculate_unit_price (diameter, price):
    pi = math.pi
    radius = diameter / 2
    square = pi * radius * radius
    euros_per_meter = price /square * 10000
    return euros_per_meter

#def Main()
diameter_pizza_first_enter = float(input("Enter the diameter of the first pizza (cm): "))
price_pizza_first_enter = float(input("Enter the price of the first pizza (euros): "))
diameter_pizza_second_enter = float(input("Enter the diameter of the second pizza (cm): "))
price_pizza_second_enter = float(input("Enter the price of the second pizza (euros): "))

price_per_meter_first = float(calculate_unit_price(diameter_pizza_first_enter, price_pizza_first_enter))
print(f"Unit price of the first pizza: {price_per_meter_first:.2f} euros/m²")
price_per_meter_second = float(calculate_unit_price(diameter_pizza_second_enter, price_pizza_second_enter))
print(f"Unit price of the second pizza: {price_per_meter_second:.2f} euros/m²")

if price_per_meter_first < price_per_meter_second:
    print("The first pizza provides better value for money.")
else:
    print("The second pizza provides better value for money.")