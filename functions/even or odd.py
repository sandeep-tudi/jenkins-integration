# Define a function called is_even that takes in one argument, and returns True if the passed-in value is even, False if it is not.

def even_odd(num):
    if num % 2 == 0:
        return True
    else:
        return False

result = even_odd(5)
print(result)