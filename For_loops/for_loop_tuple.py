# tuple packing
mylist = [(1,2),(3,4),(5,6)]    # This is a list of tuple
print(len(mylist))
print(type(mylist))
for (a,b) in mylist:            # This is called tuple unpacking
    print(a)                    # In Tuple unpacking we are taking variables which looks like tuple
    print(b)                    # Now we can get individual values of tuple