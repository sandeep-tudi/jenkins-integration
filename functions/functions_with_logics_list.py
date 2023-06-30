# returns True if any number is even inside the list
def check_even_list(num_list):
    # Return all the even numbers in the list
    for number in num_list:
        if number % 2 == 0:
            return True
        else:
            pass
    return False

result = check_even_list([2,4,6])
print(result)
