number_enter_str = input("Enter an integer: ")
number_enter = int(number_enter_str)

is_prime = True

if number_enter <= 1:
    is_prime = False
else:
    for number_to_check in range(2, int(number_enter**0.5) + 1):
        if number_enter % number_to_check == 0:
            is_prime = False
            break

if is_prime:
    print(f"{number_enter} is a prime number.")
else:
    print(f"{number_enter} is not a prime number.")