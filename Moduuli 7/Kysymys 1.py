def get_season (local_number_month_int):

    if local_number_month_int in (12, 1, 2):
        return "winter"
    elif local_number_month_int in (3, 4, 5):
        return "spring"
    elif local_number_month_int in (6, 7, 8):
        return "summer"
    elif local_number_month_int in (9, 10, 11):
        return "autumn"
    else:
        raise ValueError("The wrong month_number entered.")


number_month_int = int(input("Enter the number of a month (1-12): "))
acceptable_month_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

print(f"You entered: {number_month_int} ")

# Validation
if not number_month_int in acceptable_month_numbers:
    print("Please enter a number between 1 and 12.")
    exit()

print(f"The season is {get_season(number_month_int)}.")

