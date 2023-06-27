d = {'K1':1,'K5':2,'k7':3}

for key,values in d.items(): # Here we have used the same concept of tuple unpacking in Dictionary
    print(key,values)

for key in d.values():
    print(key)

for values in d.values():
    print(values)