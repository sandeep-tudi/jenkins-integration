def myfunc(string):
    nstr = ''
    for index in range(0,len(string)):
        if index % 2 == 0:
            nstr = nstr+(string[index].upper())
        else:
            nstr = nstr+(string[index])
    return nstr

newstr = myfunc('Sandeep')
print(newstr)