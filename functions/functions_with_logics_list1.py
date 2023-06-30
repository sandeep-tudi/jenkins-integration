# This program will check and return all the even numbers in the list
def return_even_list(num_list):
    even_list = []
    for number in num_list:
        if number % 2 == 0:
            even_list.append(number)
    return even_list

even_numbers = return_even_list([1,3,7])

print(even_numbers)

