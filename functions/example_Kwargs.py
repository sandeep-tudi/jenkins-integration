# In this program we will see how does the  kwargs work
# We can pass any number of dictinoary's using the ** kwargs

def myfunc(**kwargs):
    if 'fruit' in kwargs:
        print('My Fruit of choice is {}'.format(kwargs['fruit']))
    else:
        print("I did not find any fruit here")
    # print(kwargs)

myfunc (fruit='apple', veggie='lattice', meat = 'Chicken')