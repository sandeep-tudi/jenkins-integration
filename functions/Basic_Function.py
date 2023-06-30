def say_hello(name = 'Default'): # We can declare a parameter value as default in this way
    print(f'Hello {name}')       # If we have default value the function gets executed even when the parameter is not passed during the function call

say_hello('Sandeep')