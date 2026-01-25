import random
secret_number_int = random.randint(1,10)

while True:
    user_number_str = input("Guess a number (1-10): ")
    user_number_int = int(user_number_str)

    if user_number_int == secret_number_int:
        print("Guess a number (1-10): Correct")
        break
    if user_number_int < secret_number_int:
        print("Guess a number (1-10): Too low")
        continue
    if user_number_int > secret_number_int:
        print("Guess a number (1-10): Too high")
        continue


