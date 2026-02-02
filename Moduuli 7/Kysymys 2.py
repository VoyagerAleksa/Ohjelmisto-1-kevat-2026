names = set()

while True:
    enter_name_str = input("Please enter your name: ")
    print(enter_name_str)
    if enter_name_str == "":
        break
    if enter_name_str in names:
        print("Existing name")
    else:
        print("New name")

    names.add(enter_name_str)
for requstered_name_str in names:
    print(requstered_name_str)
