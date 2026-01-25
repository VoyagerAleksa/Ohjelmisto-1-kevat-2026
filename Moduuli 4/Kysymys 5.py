correct_username_str = "python"
correct_password_str = "rules"
counter = 0
while True:
    counter = counter + 1
    enter_username_str = input("Enter username: ")
    enter_password_str = input("Enter password: ")

    if correct_username_str == enter_username_str and correct_password_str == enter_password_str:
        print("Welcome")
        break
    else:
        if counter != 5:
            print("Incorrect username or password. Please try again.")


    if counter == 5:
        print("Access denied")
        break
