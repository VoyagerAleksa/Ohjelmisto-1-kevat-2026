number_enter_list = []
while True:
    number_enter_str = input("Enter a number: ")
    if number_enter_str == "":
        break
    number_enter_list.append  (float(number_enter_str))
    number_enter_list.sort(reverse=True)
print("The greatest numbers in descending order: ")
for num in number_enter_list [:5]:
    print(num)