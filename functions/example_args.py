# In this program we will see what does args do.
def myfunc(*args):  # Here is we specify * before the parameter we can pass any number
    return (args)   # of Variables from the functions. We can cange the args to any name
                    # There are no hard rules of the name of args its just about *

result = myfunc(10,20,30,40,50)
print(result)
