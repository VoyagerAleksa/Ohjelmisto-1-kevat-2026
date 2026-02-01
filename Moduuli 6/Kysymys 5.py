def filter_even_numbers(whole_numbers_list):
    even_numbers_list = []
    length_of_list_int = len(whole_numbers_list)

    for count_int in range(length_of_list_int):
        number_int = whole_numbers_list[count_int]
        if number_int % 2 == 0:
           even_numbers_list.append(number_int)
    return even_numbers_list

original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_list = filter_even_numbers(original_list)
print("Original list:", original_list)
print("List with even numbers only:", filtered_list)